---
title: zx
date: 2026/02/11 23:57:22
categories:
  - - Language
    - Javascript
    - Library
abbrlink: 79ba4ba
---
# ZX 

## 元信息

**Google zx** 是一个开源工具库，旨在简化使用 **JavaScript/TypeScript** 编写命令行脚本的方式，把 Node.js 的能力与类似 Shell 脚本的写法结合起来，让脚本开发更便捷、更现代化。它为常见的脚本场景提供了高效的抽象、跨平台兼容性支持以及更安全的参数转义机制。该项目托管于 GitHub，并采用 **Apache 2.0** 开源许可协议发布。([GitHub][1])

这个库最初由 Google 团队创建（目前由社区维护），并非 Google 官方产品支持，但因其极大提升了 Node 脚本可用性和可维护性而获得广泛关注。([Zenn][2])

zx 的设计哲学在于“让脚本更像代码”。传统的 Bash shell 脚本在处理复杂逻辑时往往不够直观、错误处理复杂、可维护性差，而 JavaScript 拥有成熟的语言特性与丰富生态，但原生 Node.js 对执行外部命令和参数处理的支持较为繁琐。**zx 在二者之间架设了一座桥梁**：在保持命令执行体验的同时，引入现代语言结构和异步处理方式。([google.github.io][3])

它的核心优势包括：

提供跨平台命令执行封装，自动处理参数转义与引号安全。

支持 **top-level await**（在 `.mjs` 或 ES Module 环境中），脚本可像现代 JS 代码一样编写异步逻辑。

提供常用工具函数（如 `cd()` 目录切换、`question()` 终端交互、`fetch` HTTP 调用等），减少手写样板代码。

与 Node.js 生态无缝集成，可以直接调用 npm 生态中的库和工具。([google.github.io][4])

兼容性好，可在 Linux、macOS、Windows（通过 Bash 或 PowerShell）上运行，并支持多种运行时如 Node.js、Bun、Deno 等。([GitHub][1])

---

## 安装与环境要求

要使用 zx，先通过 npm 安装依赖。在项目本地添加依赖或全局安装均可：

```bash
npm install zx
```

或

```bash
npm install -g zx
```

然后在脚本文件顶部添加 shebang 以便直接作为可执行脚本运行：

```bash
#!/usr/bin/env zx
```

这行的作用是告诉系统这个文件要交给 zx 来跑。

确保在支持 Bash 或等效 Shell 的环境下运行脚本。在 Windows 上可借助 **WSL**、Git Bash 或 PowerShell。([google.github.io][5])

---

## 使用样例与基本语法

在 `.mjs` 扩展名的脚本文件中，你可以直接使用 `$` 作为命令执行标签模板，同时支持异步执行和 Promise 组合。

下面是一个典型的 zx 脚本示例：

```javascript
#!/usr/bin/env zx

// 直接执行 shell 命令并等待完成
await $`echo "Hello from zx"`;

// 获取当前 Git 分支名
const branch = await $`git branch --show-current`;
console.log(`Current branch: ${branch.stdout.trim()}`);

// 并行执行多个命令
await Promise.all([
  $`sleep 1; echo First`,
  $`sleep 2; echo Second`,
  $`sleep 3; echo Third`,
]);

// 使用变量作为命令参数（自动转义）
const dirName = 'temp folder';
await $`mkdir -p ${dirName}`;
```

在这个例子中，``$`command` `` 表达式会执行外部命令，返回一个对象，包含标准输出、标准错误和退出码等信息。所有通过 `${…}` 注入的变量都会被自动安全转义。([google.github.io][4])

要使用 top-level await，需要将脚本保存为 **.mjs** 并确保运行时环境支持 ES Modules。如果使用 `.js` 扩展名，则需包装 `await` 到异步函数中。([google.github.io][4])

---

## 运行脚本

如果你有`test-script.mjs`，你可以通过`zx test-script.mjs` or `test-script.mjs` 来运行，通过后者运行需要配合上文说过的shebang

## 进阶功能与扩展

除了基本的命令执行，zx 还提供一些能够简化脚本开发的功能：

可以直接访问诸如 **fetch**（用于 HTTP 请求）、**chalk**（用于彩色终端输出）、**minimist**（命令行参数解析）等常用库。

支持 `cd()` 修改工作目录，对需要路径切换的脚本尤为方便。

可捕获命令失败并进行异常处理，增强脚本鲁棒性。

可与 TypeScript 一起使用，通过添加类型定义提升开发体验。([google.github.io][5])

---

## 典型应用场景

Google zx 适合用于自动化任务、CI/CD 流程脚本、项目构建与部署流程、定期维护任务处理等场景。相比传统 Shell 脚本，它更适合需要复杂逻辑控制、错误处理和第三方库集成的脚本项目。([Software Testing and Development Company][6])

---

## 许可与社区

zx 采用 **Apache-2.0** 开源许可协议发布，欢迎开发者在遵循协议的前提下 Fork、贡献或用于商业项目。项目在 GitHub 上拥有活跃的社区、讨论和丰富的示例集，可根据需要查阅官方文档进一步深入学习。([GitHub][1])

---

如需查看完整文档、API 参考或更多示例代码，可以访问项目官方文档站点。([google.github.io][3])

若需要我进一步整理更完整的用法示例、最佳实践或在实际工程中的应用案例，也可以继续提出。

[1]: https://github.com/google/zx?utm_source=chatgpt.com "google/zx: A tool for writing better scripts"
[2]: https://zenn.dev/overflow_offers/articles/20220606-zx-introduction?utm_source=chatgpt.com "zxの紹介 〜 さよならシェルスクリプト そして伝説へ｜Offers ..."
[3]: https://google.github.io/zx/?utm_source=chatgpt.com "google/zx"
[4]: https://google.github.io/zx/getting-started?utm_source=chatgpt.com "Getting Started | google/zx"
[5]: https://google.github.io/zx/setup?utm_source=chatgpt.com "Setup | google/zx"
[6]: https://shiftasia.com/community/discovering-zx-a-good-choice-to-replace-bash-scripts/?utm_source=chatgpt.com "Discovering zx: A Good Choice to Replace Bash Scripts"
