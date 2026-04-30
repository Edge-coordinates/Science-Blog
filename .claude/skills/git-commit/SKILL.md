---
name: git-commit
description: >
  Generate well-formatted Git commit messages following conventional commit standards,
  adapted for this blog/notes repository (adds `notes` and `diary` types and a
  `(YYYYMMDD)` date-scope convention for content commits).
  Use this skill whenever the user asks to commit changes, write a commit message, stage and commit,
  or says anything like "commit this", "generate a commit", "what should my commit message be",
  or "help me commit". Also trigger when the user is done with a coding task and naturally
  needs to save their work. Auto-detects the commit type from staged changes but always allows
  the user to override.
---

# Git Commit Message Skill

> **Repo context:** this is a blog / technical-notes repository. Most commits add or expand
> Markdown notes under `Environment/`, `Framework/`, `Language/`, `AI/`, `Agent/`, `Production/`,
> `Life/`, or `Diary/`. The conventions below are tuned for that — **content commits use
> `notes` / `diary` with a `(YYYYMMDD)` scope**, while tooling/config commits keep the
> standard conventional-commit types.

## Workflow

### Step 1 — Check for staged changes

Run:
```bash
git diff --cached --stat
```

- If nothing is staged → warn the user: *"No files are staged. Please use `git add` to stage your changes first."* Then stop.
- If staged → proceed.

### Step 2 — Inspect the diff

Run both:
```bash
git diff --cached --stat
git diff --cached
```

Use the stat for a high-level overview (files changed, insertions, deletions).
Use the full diff to understand *what* and *why*.

### Step 3 — Check for merge commit

Run:
```bash
cat .git/MERGE_HEAD 2>/dev/null
```

If a merge is in progress, generate a merge commit message instead — see **Merge Commits** section below.

### Step 4 — Assess commit scope

If the diff touches **truly unrelated concerns** (e.g., tooling/config change mixed with content notes, or a bug fix mixed with a new feature), suggest splitting:

> "This diff seems to cover multiple concerns: [X, Y, Z]. Would you like me to suggest how to split these into separate commits?"

If the user says yes → list the proposed splits and stop. Let the user stage the first batch before proceeding.

**Blog repo exception:** multiple unrelated **notes** in one commit is normal and OK
(e.g., a Linux note + a React note + a diary entry on the same day). Don't suggest
splitting just because the topics differ — only split when content commits are mixed
with config/tooling commits.

Otherwise, continue with a single commit.

### Step 5 — Auto-detect commit type

Use the table below to infer the type from filenames, content, and patterns. Pick the best fit.

**Blog content types (most common for this repo):**

| Type     | Signals                                                                                |
| -------- | -------------------------------------------------------------------------------------- |
| `notes`  | New / expanded `.md` notes under `Environment/`, `Framework/`, `Language/`, `AI/`, `Agent/`, `Production/`, `Life/`, or any topical folder. Default for content. |
| `diary`  | Entries under `Diary/` (e.g. `Diary/2026/0211 日记.md`)                                 |

**Tooling / repo types (less common — for non-content changes):**

| Type       | Signals                                                                       |
| ---------- | ----------------------------------------------------------------------------- |
| `chore`    | `.vscode/settings.json`, `.gitignore`, build/tooling configs, deps            |
| `skill`    | Adding or editing files under `.claude/skills/`                               |
| `docs`     | `README.md`, top-level repo documentation (NOT content notes — those are `notes`) |
| `fix`      | Fixing a broken link, abbrlink, frontmatter, build error in the repo itself   |
| `feat`     | New repo-level capability (rare — e.g. a new build script, theme feature)     |
| `refactor` | Repo-wide reorganization, file moves/renames without content change           |
| `style`    | Formatting only                                                               |
| `test`     | Test files (rare in this repo)                                                |
| `perf`     | Performance changes (rare in this repo)                                       |

**Disambiguation rules:**
- A new `.md` file under a content folder → `notes`, **not** `docs`. (`docs` is reserved for repo-level docs like `README.md`.)
- Edits inside `Diary/` → always `diary`, even for short entries.
- Mixed content + tooling diff → suggest splitting (see Step 4).

Present the auto-detected type to the user and invite override:
> "I've detected this as a `notes` commit. Let me know if you'd like a different type."

### Step 6 — Generate the commit message

Follow the format:

```
<type>(<scope>): <title>

[optional body — usually omitted for content commits]
```

**Scope rules:**
- For `notes` and `diary` → scope is the **commit date in `YYYYMMDD`** form
  (e.g. `notes(20260430): ...`). Use today's date unless the user specifies otherwise.
- For `chore` / `feat` / `fix` / `skill` / etc. → scope is an **area name** if helpful
  (`chore(vscode): ...`, `skill(git-commit): ...`), or omitted entirely (`skill: add ...`).
- Date scope and area scope don't mix. Pick one based on the type.

**Title rules:**
- **English** — even when filenames or content are Chinese, the commit subject is English.
  Topic names with no good English equivalent may stay in their original language
  (e.g. a game title `求生之路2`), but connectors are English.
- Lowercase first letter, no period at end.
- Aim for ≤70 characters (a bit looser than the standard 50, because multi-topic blog
  commits often need to list 2–4 topics).
- For multi-topic content commits, list main topics separated by commas, optionally
  ending with `and more` if you abbreviated:
  `notes(20260223): ComfyUI install, AI prompts, React animations and more`
- Specific over generic — never just `update` or `add notes`.

**Body rules:**
- **Default to no body** for `notes` / `diary` / `chore` commits — the title already
  conveys the topic list.
- Add a body only when the change has non-obvious reasoning, a tricky bug fix,
  or a single deep-dive note that benefits from a 1–2 line summary.
- When used: bullet points, concise, explain *why* not just *what*.

**Never** append any co-authorship, attribution, or AI-generated trailer to the commit message, regardless of the tool or environment.

### Step 7 — Present message and ask: commit or modify?

After generating the commit message, always display it in a code block, then ask:

> "Commit with this message, or would you like to modify it?"

**If user confirms (yes / lgtm / commit / ok / 好 / 確認 / etc.):**
- In CLI / Claude Code (bash tools available) → run: `git commit -m "<title>" -m "<body>"`
- In web / chat (no bash) → display the message again in a copyable block and instruct: *"Run: `git commit -m '...'`"*
- Never run the commit before the user explicitly confirms.

**If user wants to modify:**
- Accept their feedback (e.g. "change the type to fix", "make the title shorter", "add a scope").
- Regenerate the message incorporating their feedback.
- Return to the top of Step 7 — show the updated message and ask again.
- Repeat until the user confirms or abandons.
- Never argue with the user's requested changes.

---

## Merge Commits

If a merge is in progress:

```
merge(<branch>): merge <source-branch> into <target-branch>

- Resolved conflicts in: <files if any>
- <any notable integration notes>
```

Keep it factual. Don't over-explain standard merges.

---

## Edge Case Reference

| Situation                            | Action                                                        |
| ------------------------------------ | ------------------------------------------------------------- |
| Nothing staged                       | Warn and stop. Do not proceed.                                |
| Content + tooling mixed              | Suggest splitting (`notes` vs `chore`); don't combine         |
| Multiple unrelated notes             | OK — combine into one `notes(YYYYMMDD)` commit, list topics   |
| Only whitespace/formatting           | Use `style` type                                              |
| README / repo-level doc change       | Use `docs` (NOT `notes` — that's for content)                 |
| `.md` under content folder           | Use `notes` (NOT `docs`)                                      |
| File under `Diary/`                  | Use `diary` always                                            |
| File under `.claude/skills/`         | Use `skill`                                                   |
| Ambiguous type                       | Auto-detect best guess, invite override                       |
| Merge in progress                    | Use merge commit format                                       |
| User dislikes generated message      | Regenerate with their feedback; never argue                   |

---

## Format Quick Reference

**Blog content (most common):**

```
notes(20260223): ComfyUI install, AI prompts, React animations and more
```

```
notes(20260214): JS particle case sensitivity, React Compiler pitfalls
```

```
notes(20260330): how to use git worktree with Claude Code
```

```
diary(20260211): daily log
```

**Tooling / repo:**

```
chore(20260430): update VSCode settings and icon library notes
```

```
skill: add discuss-first git-commit skill
```

```
fix: readme abbrlink error
```

**With body (rare — only when reasoning matters):**

```
notes(20260214): React Compiler pitfalls

- Documented the case-sensitivity issue that broke production builds on Linux
  but worked locally on macOS
```
