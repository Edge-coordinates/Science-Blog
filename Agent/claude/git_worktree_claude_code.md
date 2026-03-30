[toc]

# Git Worktree with Claude Code

### A Complete Usage Guide
*Parallel development workflows without stashing or branch switching*

---

## 1. Overview

Git Worktree is a built-in Git feature that lets you check out multiple branches simultaneously, each in its own dedicated directory, while sharing a single `.git` repository. When used together with Claude Code, it enables parallel, isolated AI-assisted development sessions — each session working on a different branch without interfering with one another.

### 1.1 Why Use Worktrees?

Traditional git workflow forces you to stash changes, switch branches, work, then switch back. Every context switch disrupts your flow. Worktrees solve this by giving each task a permanent, isolated directory:

- No stashing — each worktree has its own working tree and index.
- Run multiple Claude Code sessions simultaneously on different features.
- Keep a stable main branch always ready to read or run.
- Drastically reduce cognitive overhead when juggling multiple tasks.

### 1.2 How Worktrees Relate to Claude Code

Claude Code is a terminal-based AI coding agent. Because it operates on the filesystem inside a directory, it respects worktree boundaries naturally. You can:

- Open a separate terminal tab for each worktree.
- Start a dedicated Claude Code session per tab with `claude`.
- Let Claude work independently on each feature without cross-contamination.

> **Key Concept:** A worktree is NOT a clone — it shares the same `.git` database. Creating 5 worktrees uses almost no extra disk space for the repo history. Only the working files are separate.

---

## 2. Prerequisites

- Git 2.5 or later (worktrees were introduced in 2.5).
- Claude Code installed: `npm install -g @anthropic-ai/claude-code` (requires Node.js 18+).
- A local Git repository with at least one commit.
- Familiarity with basic Git concepts (branches, commits, merges).

---

## 3. Core Concepts

### 3.1 Linked Worktree vs Main Worktree

Every repository has exactly one **main worktree** (where `.git/` lives). All additional worktrees created with `git worktree add` are called **linked worktrees**. They store a small `.git` file (not a directory) pointing back to the main repository's object database.

### 3.2 Branch Exclusivity

Git enforces that a branch can be checked out in **at most one worktree at a time**. Attempting to check out a branch that is already checked out elsewhere will produce an error. This prevents accidental conflicts between worktree sessions.

> **Important:** If you try to check out the same branch in two worktrees, Git will refuse with:
> ```
> fatal: 'feature/my-branch' is already checked out at '/path/to/other-worktree'
> ```
> Always use distinct branch names per worktree.

---

## 4. Creating a Worktree Based on Your Latest Local Commit

The most common scenario is creating a new worktree that starts from where your current work is — the latest commit on your main (or current) branch.

### 4.1 Verify Your Starting Point

```bash
# Show current branch and last commit
git log --oneline -5

# Make sure everything is committed (no dirty state on main)
git status
```

### 4.2 Create the Worktree with a New Branch

```bash
# Syntax: git worktree add <path> -b <new-branch> [<start-point>]

# Create from the current HEAD (latest local commit):
git worktree add ../my-project-feature -b feature/my-feature

# Create from a specific branch tip:
git worktree add ../my-project-fix -b fix/critical-bug main

# Create from a specific commit hash:
git worktree add ../my-project-exp -b experiment/alpha abc1234
```

Use a **sibling directory** (`../project-feature`) to keep worktrees organised alongside your main repo:

```
~/projects/
  my-project/          ← main worktree (.git lives here)
  my-project-feature/  ← linked worktree for feature/my-feature
  my-project-fix/      ← linked worktree for fix/critical-bug
```

### 4.3 What Happens Under the Hood

- Git creates the directory at the specified path.
- It creates a `.git` file (not folder) inside that directory pointing to the main repo.
- A new branch is created at the specified start point (defaults to HEAD).
- The branch is checked out into the new directory.
- The new branch is registered in `.git/worktrees/` inside the main repo.

### 4.4 Open Claude Code in the New Worktree

```bash
# In a new terminal tab:
cd ../my-project-feature

# Start Claude Code
claude

# Or for trusted projects (skips permission prompts):
claude --dangerously-skip-permissions
```

> **Pro Tip:** Use terminal multiplexers like `tmux` or iTerm2 with named panes:
> ```
> Pane 1: cd ~/projects/my-project       && claude   (main branch — read-only reference)
> Pane 2: cd ~/projects/my-project-feat  && claude   (feature branch — active development)
> Pane 3: cd ~/projects/my-project-fix   && claude   (hotfix branch — urgent fix)
> ```

---

## 5. Making Commits Inside a Worktree

Once inside a linked worktree, all standard Git commands work exactly as expected. The worktree has its own index (staging area) and working tree, completely isolated from other worktrees.

### 5.1 Normal Commit Workflow

```bash
# Navigate to the worktree
cd ../my-project-feature

# Stage changes
git add .
# or selectively:
git add src/components/Button.tsx

# Commit
git commit -m "feat: add responsive button component"

# Check status
git log --oneline -3
```

### 5.2 Committing from Within Claude Code

You can ask Claude Code to commit directly. Inside the worktree directory, Claude will use the correct branch automatically:

```
> Please implement the search filter component, then commit the changes
>   with a conventional commit message.
```

Claude Code will run `git add`, write a commit message, and execute `git commit` on your behalf. Because it is running inside the linked worktree directory, it commits to `feature/my-feature` — not `main`.

### 5.3 Pushing the Branch to Remote

```bash
# From within the worktree directory:
git push -u origin feature/my-feature

# Subsequent pushes (tracking is set):
git push
```

---

## 6. Listing and Inspecting Worktrees

```bash
# List all worktrees for the current repository:
git worktree list

# Example output:
# /Users/alice/projects/my-project          a3f91bc [main]
# /Users/alice/projects/my-project-feature  d4e82ca [feature/my-feature]
# /Users/alice/projects/my-project-fix      a3f91bc [fix/critical-bug]

# Verbose output with full details:
git worktree list --porcelain
```

---

## 7. Merging the Worktree Branch Back Into Main

When your feature or fix is ready, you have two primary strategies for integrating it back into `main`:

| Strategy | History Shape | Merge Commit? | Best For |
|---|---|---|---|
| Merge (`--no-ff`) | Diverges + converges | Yes | Shared branches, full auditability |
| Rebase + FF | Linear | No | Clean PRs, solo branches |
| Squash Merge | Linear, single commit | No | Keeping main pristine |

---

### Strategy A: Merge Commit — Preserving Branch History (Diverge + Converge)

A standard `git merge` creates a merge commit that explicitly records the point where two diverged histories converged. This is the safest strategy and is preferred for shared, long-lived branches.

**Step 1 — Ensure the feature branch is ready**

```bash
cd ../my-project-feature

git status              # must be clean
git log --oneline -5   # verify your commits look right
git push origin feature/my-feature
```

**Step 2 — Switch to main and pull latest changes**

```bash
cd ../my-project

git checkout main
git pull origin main
```

**Step 3 — Merge the feature branch**

```bash
# Merge with an explicit merge commit (no fast-forward):
git merge --no-ff feature/my-feature -m "Merge feature/my-feature into main"

# If you want a fast-forward when possible (linear if no divergence):
git merge feature/my-feature
```

**Step 4 — Resolve conflicts (if any)**

```bash
# Git will mark conflicted files with <<<<<<<, =======, >>>>>>>
# Edit the files to resolve, then:
git add <resolved-file>
git merge --continue

# Or abort and start over:
git merge --abort
```

**Step 5 — Push main**

```bash
git push origin main
```

**Resulting history graph:**

```
* 9f4a1bc (main) Merge feature/my-feature into main
|\
| * d4e82ca feat: add responsive button component
| * c3d71ab feat: add button props interface
|/
* a3f91bc Initial commit (the shared start point)
```

---

### Strategy B: Rebase — Linear History (Replay Without Divergence)

A rebase moves your feature commits on top of the latest `main`, rewriting them so the history appears linear. There are no merge commits. This is ideal for clean pull request histories or personal feature branches not yet shared with others.

> **Warning:** Never rebase branches that have already been pushed and shared with other developers. Rewriting shared history forces others to do a hard reset. Only rebase private or PR branches.

**Step 1 — Rebase the feature branch onto main**

```bash
cd ../my-project-feature

# Fetch latest main first:
git fetch origin main

# Rebase: replay our commits on top of origin/main:
git rebase origin/main

# Interactive rebase (squash/edit/reorder commits before integrating):
git rebase -i origin/main
```

**Step 2 — Resolve conflicts during rebase**

```bash
# If a conflict occurs, Git pauses at the offending commit.
# Fix the conflict in your editor, then:
git add <resolved-file>
git rebase --continue

# Skip a particular commit (use with care):
git rebase --skip

# Abort and return to the original state:
git rebase --abort
```

**Step 3 — Fast-forward main to include the rebased branch**

```bash
cd ../my-project

git checkout main
git pull origin main        # ensure main is up-to-date

# Fast-forward merge (no merge commit needed — history is linear):
git merge feature/my-feature

git push origin main
```

**Resulting history graph:**

```
* d4e82ca' (main) feat: add responsive button component  ← rebased copy
* c3d71ab' feat: add button props interface               ← rebased copy
* a3f91bc Initial commit

# Note the ' marks — commits are rewritten with new hashes.
```

---

### Strategy C: Squash Merge — Collapse All Commits into One

A squash merge condenses all commits from the feature branch into a single staged change, which you then commit manually onto `main`. The individual commit history is discarded. This keeps `main`'s history extremely clean.

```bash
cd ../my-project
git checkout main
git pull origin main

# Squash all feature commits into the working tree (staged, not committed):
git merge --squash feature/my-feature

# Commit with a single descriptive message:
git commit -m "feat: add responsive button component with props (#42)"

git push origin main
```

---

## 8. Comparison of Integration Strategies

| **Strategy** | **History Shape** | **Merge Commit?** | **Best For** |
| --- | --- | --- | --- |
| Merge (--no-ff) | Diverges + converges | Yes | Shared branches, full auditability |
| Rebase + FF | Linear | No | Clean PRs, solo branches |
| Squash Merge | Linear, single commit | No | Keeping main pristine |

## 9. Removing a Worktree After Merging

```bash
# From the main worktree directory (or anywhere in the repo):
git worktree remove ../my-project-feature

# If the worktree has untracked or uncommitted changes, force removal:
git worktree remove --force ../my-project-feature

# Prune stale references (e.g., if you deleted the directory manually):
git worktree prune

# Optionally delete the branch as well:
git branch -d feature/my-feature
git push origin --delete feature/my-feature
```

---

## 10. Full End-to-End Example

**Scenario:** Add a dark-mode toggle while a hotfix is in progress.

**Step 1 — Check current state**

```bash
cd ~/projects/my-app
git log --oneline -3
# e7a3c1b (HEAD -> main, origin/main) chore: update dependencies
# 4f92d88 feat: add user profile page
# 1a8bc34 init: scaffold project
```

**Step 2 — Create two worktrees from HEAD**

```bash
git worktree add ../my-app-darkmode  -b feature/dark-mode
git worktree add ../my-app-hotfix    -b fix/login-crash

git worktree list
# ~/projects/my-app          e7a3c1b [main]
# ~/projects/my-app-darkmode e7a3c1b [feature/dark-mode]
# ~/projects/my-app-hotfix   e7a3c1b [fix/login-crash]
```

**Step 3 — Work on both in parallel with Claude Code**

```bash
# Terminal tab 1 — dark mode feature:
cd ~/projects/my-app-darkmode && claude
> Implement a dark-mode toggle that persists in localStorage.

# Terminal tab 2 — hotfix:
cd ~/projects/my-app-hotfix && claude
> Fix the login crash when email contains a + character.
```

**Step 4 — Commit in each worktree independently**

```bash
# In my-app-hotfix (fix is urgent, merge first):
git add src/auth/login.ts
git commit -m "fix: handle + character in email during login"
git push origin fix/login-crash
```

**Step 5 — Merge the hotfix (fast-forward, linear history)**

```bash
cd ~/projects/my-app
git checkout main
git pull origin main
git merge fix/login-crash
git push origin main
```

**Step 6 — Rebase dark-mode onto updated main**

```bash
cd ~/projects/my-app-darkmode
git fetch origin main
git rebase origin/main   # replays dark-mode commits on top of the hotfix
```

**Step 7 — Merge dark-mode with a merge commit (to preserve history)**

```bash
cd ~/projects/my-app
git merge --no-ff feature/dark-mode -m "Merge feature/dark-mode into main"
git push origin main
```

**Step 8 — Clean up**

```bash
git worktree remove ../my-app-darkmode
git worktree remove ../my-app-hotfix
git branch -d feature/dark-mode fix/login-crash
git push origin --delete feature/dark-mode fix/login-crash
```

---

## 11. Quick Reference

| Command | Description |
|---|---|
| `git worktree add <path> -b <branch>` | Create new worktree with a new branch from HEAD |
| `git worktree add <path> -b <branch> <start>` | Create from specific branch or commit |
| `git worktree list` | List all worktrees |
| `git worktree list --porcelain` | Machine-readable worktree details |
| `git worktree remove <path>` | Remove a linked worktree |
| `git worktree remove --force <path>` | Force-remove even with uncommitted changes |
| `git worktree prune` | Remove stale worktree metadata |
| `git merge --no-ff <branch>` | Merge with explicit merge commit |
| `git merge --squash <branch>` | Collapse branch into staged changes |
| `git rebase origin/main` | Rebase current branch onto remote main |
| `git rebase -i origin/main` | Interactive rebase (squash, edit, reorder) |
| `git branch -d <branch>` | Delete local branch after merging |
| `git push origin --delete <branch>` | Delete remote branch |

---

## 12. Troubleshooting

**Branch already checked out**

```
fatal: 'feature/my-feature' is already checked out at '/path/to/worktree'
```

Solution: use a different branch name, or remove the existing worktree first with `git worktree remove /path/to/worktree`.

**Detached HEAD in a worktree**

If you created a worktree without `-b`, it enters detached HEAD state. Create a branch to stabilise it:

```bash
git switch -c feature/my-new-branch
```

**Rebase conflicts with many commits**

When rebasing a long-lived branch, squash your commits first to reduce conflict surface area:

```bash
git rebase -i HEAD~N     # squash N commits into one
git rebase origin/main   # then rebase the single commit
```

**Claude Code editing the wrong branch**

Always verify the branch before starting Claude Code:

```bash
cd ../my-project-feature
git branch --show-current   # must show: feature/my-feature
claude
```

---

## 13. Best Practices

- Name worktree directories after their branches for clarity (`my-app-feature-dark-mode`).
- Keep worktrees as siblings of the main repo, not nested inside it.
- Always commit or stash inside a worktree before removing it — `git worktree remove` will refuse if there are local changes.
- Use `git worktree prune` periodically to clean stale references from deleted directories.
- Prefer `merge --no-ff` for team branches to preserve history; use rebase only on private branches.
- Run `git fetch` inside each worktree independently — fetch does not automatically propagate across worktrees.
- For long-running features, periodically rebase onto `main` to minimise merge conflicts later.

---

## 14. Summary

Git Worktree combined with Claude Code creates a powerful parallel development environment. Each worktree is a fully functional Git checkout — commits, pushes, rebases, and merges all work exactly as on any normal branch.

1. Create a worktree from the latest local commit with `git worktree add <path> -b <branch>`.
2. Open a separate Claude Code session (`claude`) inside each worktree directory.
3. Commit and push from within the worktree — it always operates on the correct branch.
4. Integrate back into `main` using a **merge commit** (diverge + converge), a **rebase** (linear), or a **squash merge** (single commit).
5. Clean up with `git worktree remove` and `git branch -d` once merged.

> Git Worktrees do not replace your understanding of branches — they amplify it. Every workflow that works with branches works equally well with worktrees. The only constraint is that each branch can live in at most one worktree at a time.
