---
title: monorepo中跨包导入问题
date: 2026/02/23 17:16:19
categories:
  - - Language
    - Javascript
    - Typescript
abbrlink: 1a1a74e9
---
Error is gone. Here's the full explanation of everything at play:

---

## Summary: TypeScript + `package.json` exports in monorepo

### Why the error occurred

Your `tsconfig.base.json` has `composite: true`, which implies **all source files must be under `rootDir`** (defaults to the tsconfig's directory). When TypeScript resolves `@package/ui/Navigation` via the `exports` field → `./src/Navigation/index.ts`, that file lives in `package/ui/`, which is outside `package/app/`'s `rootDir`. Hence the error.

Additionally, `include: ["../ui/**/*.ts"]` was directly pulling ui source into app's program — a double violation.

### How TypeScript resolves `package.json` exports

With `moduleResolution: "Bundler"` (your base config), TypeScript **fully supports** the `exports` field:

1. `import {RouterLink} from '@package/ui/Navigation'`
2. TS finds `@package/ui` → reads `package.json`
3. Matches `exports["./Navigation"]` → uses `types` condition → `./src/Navigation/index.ts`
4. Resolution succeeds

The issue was never about `exports` compatibility — it was about `composite`'s `rootDir` enforcement.

### What was changed

**`package/app/tsconfig.json`:**
- Overrode `composite: false`, `declaration: false`, `declarationMap: false`, `emitDeclarationOnly: false` — app is a leaf Vite application, not a library, so it doesn't need these
- Removed `"../ui/**/*.ts", "../ui/**/*.tsx"` from `include` — app should only compile its own source; cross-package types come through `exports` resolution
- Removed `outDir` since app doesn't emit anything (Vite handles bundling)

**Root `tsconfig.json`:**
- Removed `app` from `references` — without `composite`, it can't participate in `tsc -b`

### The pattern for extensionless cross-package imports

Your current `package/ui/package.json` exports setup is correct for this:

```9:16:package/ui/package.json
    "./*": {
      "types": "./src/*",
      "import": "./src/*"
    },
    "./Navigation": {
      "types": "./src/Navigation/index.ts",
      "import": "./src/Navigation/index.ts"
    }
```

- **Wildcard `./*`** — handles extensionless file imports like `@package/ui/SomeFile`
- **Explicit `./Navigation`** — needed for directory-based exports (where the actual file is `index.ts` inside a folder), because the wildcard won't automatically append `/index.ts`

The rule: **for any directory with an `index.ts`, add an explicit `exports` entry**. Wildcards only work for direct file-to-file mapping.