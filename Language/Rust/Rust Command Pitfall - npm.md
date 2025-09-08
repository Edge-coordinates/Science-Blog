---
title: Rust Command Pitfall - npm
date: 2025/3/22 16:4:13
categories:
  - - Language
    - Rust
abbrlink: ba6b9fd1
---

when you code, meet this error

```powershell
error: failed to run custom build command for ``                 

Caused by:
  process didn't exit successfully: `..\build-script-build` (exit code: 101)
  --- stderr

  thread 'main' panicked at build.rs:8:10:
  Failed to run pnpm build: Error { kind: NotFound, message: "program not found" }      
  note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

The reason is explained clearly by this blog: https://stackoverflow.com/questions/78242352/why-i-get-program-not-found-error-on-running-npm-v-command-with-rust-command  

to solve it, write this function bellow

```rust
pub fn npm() -> Command {
    #[cfg(windows)]
    const NPM: &str = "npm.cmd";
    #[cfg(not(windows))]
    const NPM: &str = "npm";

    Command::new(NPM)
}
```