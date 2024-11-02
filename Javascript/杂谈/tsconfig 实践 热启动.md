---
title: tsconfig 实践 热启动
date: 2024/11/2 23:22:27
categories:
  - [Javascript, 杂谈]
---
> ts-node 是干什么的

ts-node是一个命令行工具，用于在Node.js环境下运行TypeScript代码。通常情况下，在Node.js中运行TypeScript需要先将TypeScript代码编译成JavaScript代码，然后再用Node.js去执行编译后的JavaScript代码。而使用ts-node则可以直接运行TypeScript代码，而无需先编译成JavaScript代码。

ts-node使用TypeScript自带的编译器，可以直接将TypeScript代码解析为JavaScript代码并执行。它还提供了一些额外的功能，例如支持在REPL中直接使用TypeScript代码进行交互式开发，支持动态模块导入等。

需要注意的是，由于ts-node在运行时需要对TypeScript代码进行解析和编译，所以相比于直接运行JavaScript代码，它的启动速度可能会稍慢一些。但是，在开发阶段中，使用ts-node可以提高开发效率，同时也能避免手动进行编译的烦恼。

> 热重启的 typescript express 开发环境要怎么配置

在 TypeScript Express 开发环境中使用热重启，需要使用 `nodemon`、`ts-node` 和 `tsconfig-paths` 等工具来配合实现。具体步骤如下：

1.  安装依赖

在项目根目录下执行以下命令安装所需依赖：

`npm install nodemon ts-node tsconfig-paths -D`

2.  配置 `tsconfig.json`

在 `tsconfig.json` 文件中添加以下配置：

json

```json
{
  "compilerOptions": {
    "module": "commonjs",
    "esModuleInterop": true,
    "target": "es6",
    "outDir": "./build",
    "baseUrl": ".",
    "paths": {
      "*": ["node_modules/*", "src/types/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "**/*.spec.ts"]
}
```

其中：

*   `esModuleInterop` 配置为 `true`，使 TypeScript 可以正确地与 CommonJS 模块交互；
*   `baseUrl` 配置为 `.`，指定了默认的路径解析规则；
*   `paths` 配置用于解析路径，其中 `"*": ["node_modules/*", "src/types/*"]` 表示任意路径都会先在 `node_modules` 和 `src/types` 目录下寻找。

3.  配置 `nodemon`

在项目根目录下创建 `nodemon.json` 文件，并添加以下配置：

json

```json
{
  "watch": ["src"],
  "ext": "ts",
  "ignore": ["src/**/*.spec.ts"],
  "exec": "ts-node -r tsconfig-paths/register ./src/index.ts"
}
```

其中：

*   `watch` 配置用于指定监视文件变化的目录；
*   `ext` 配置用于指定监视的文件扩展名；
*   `ignore` 配置用于指定不需要监视的文件；
*   `exec` 配置用于指定在重启应用程序时要执行的命令，其中 `-r tsconfig-paths/register` 参数用于在运行时使用 `tsconfig-paths` 来解析路径。

4.  配置 `package.json`

在 `package.json` 文件中添加以下脚本：

json

```json
{
  "scripts": {
    "start": "nodemon",
    "build": "tsc"
  }
}
```

其中：

*   `start` 命令使用 `nodemon` 启动应用程序，并实现热重启；
*   `build` 命令用于将 TypeScript 代码编译成 JavaScript 代码，生成的代码会保存在 `./build` 目录下。

现在你就可以使用 `npm run start` 启动应用程序了。当你修改了代码后，`nodemon` 会自动重启应用程序，使修改生效。

> 继续

5.  编写 TypeScript 代码

在 `src` 目录下编写 TypeScript 代码，例如：

typescript

```typescript
import express from 'express';

const app = express();

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

这是一个简单的 Express 应用程序，当访问根路径时会返回一个 "Hello, World!" 的响应。

6.  启动应用程序

执行 `npm run start` 命令启动应用程序。当你修改代码后，`nodemon` 会自动重启应用程序，使修改生效。

访问 [http://localhost:3000，你应该能看到](http://localhost:3000%EF%BC%8C%E4%BD%A0%E5%BA%94%E8%AF%A5%E8%83%BD%E7%9C%8B%E5%88%B0) "Hello, World!" 的响应。

以上就是在 TypeScript Express 开发环境中使用热重启的配置方法。通过这种方式，你可以方便地进行开发，并且在修改代码后不需要手动重启应用程序。

> 之后的所有的回答请使用yarn作为包管理器，谢谢。

好的，后续的回答我会使用 Yarn 作为包管理器。

> 给出一个比较适合用来作后端开发的 tscongfig 配置

以下是一个比较适合用来作后端开发的 `tsconfig.json` 配置：

json

```json
{
  "compilerOptions": {
    "target": "es2020",
    "module": "commonjs",
    "lib": ["es2020"],
    "allowJs": false,
    "checkJs": false,
    "sourceMap": true,
    "outDir": "dist",
    "rootDir": "src",
    "esModuleInterop": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationDir": "types",
    "strict": true,
    "noImplicitAny": true,
    "noImplicitThis": true,
    "strictFunctionTypes": true,
    "strictNullChecks": true,
    "strictPropertyInitialization": true,
    "noImplicitReturns": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    "forceConsistentCasingInFileNames": true
  },
  "exclude": ["node_modules"],
  "include": ["src/**/*.ts"],
  "references": []
}
```

其中：

*   `target`：编译目标为 ES2020。
*   `module`：输出模块为 CommonJS。
*   `lib`：使用 ES2020 标准库。
*   `allowJs`：不允许编译 JavaScript 文件。
*   `checkJs`：不检查 JavaScript 文件。
*   `sourceMap`：生成 sourcemap。
*   `outDir`：输出目录为 `dist`。
*   `rootDir`：源代码目录为 `src`。
*   `esModuleInterop`：允许导入 CommonJS 模块。
*   `resolveJsonModule`：允许导入 JSON 文件。
*   `declaration`：生成类型声明文件。
*   `declarationDir`：类型声明文件的输出目录为 `types`。
*   `strict`：启用严格模式。
*   `noImplicitAny`：禁止隐式的 any 类型。
*   `noImplicitThis`：禁止隐式的 this 类型。
*   `strictFunctionTypes`：函数类型的参数受到严格的检查。
*   `strictNullChecks`：禁止 null 和 undefined 类型的赋值。
*   `strictPropertyInitialization`：类的属性必须在构造函数中初始化。
*   `noImplicitReturns`：函数必须显式返回类型。
*   `noUnusedLocals`：禁止未使用的局部变量。
*   `noUnusedParameters`：禁止未使用的函数参数。
*   `experimentalDecorators`：启用实验性装饰器。
*   `emitDecoratorMetadata`：启用装饰器元数据的生成。
*   `forceConsistentCasingInFileNames`：禁止大小写不一致的文件名。

这个配置文件启用了 TypeScript 的严格模式，并禁止了一些常见的 TypeScript 编程错误。同时，它也会生成类型声明文件，便于其他开发人员在使用你的代码时能够获得更好的类型提示。

> 那么你认为 tsconfig 是设置松一点还是严格一些比较好

对于 TypeScript 的 `tsconfig.json` 配置，应该根据具体项目的需求进行配置，既不能过于严格，也不能过于松散。

过于严格的配置可能会导致编译错误，使开发过程变得困难，而过于松散的配置则可能导致代码质量下降，难以维护。

一般来说，在一个新项目中，应该先采用比较严格的配置，并根据实际情况逐步放宽一些限制。例如，可以先开启严格模式，禁用隐式的 any 类型，并启用一些常见的 TypeScript 编程错误检查。如果在开发过程中发现某些错误不是真正的错误，可以逐步调整配置，放宽限制。

另外，也可以参考社区的一些最佳实践来配置 TypeScript 的 `tsconfig.json` 文件，以便保证代码质量和可维护性。

> 给出一个社区的最佳实践的示例呗，谢谢

以下是一份社区推荐的 TypeScript `tsconfig.json` 文件的示例：

json

```json
{
  "compilerOptions": {
    "target": "es2019",
    "module": "commonjs",
    "lib": ["es2019"],
    "outDir": "dist",
    "rootDir": "src",
    "strict": true,
    "esModuleInterop": true,
    "resolveJsonModule": true,
    "sourceMap": true,
    "declaration": true,
    "moduleResolution": "node",
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "strictNullChecks": true,
    "noImplicitReturns": true,
    "noImplicitThis": true,
    "noImplicitAny": false,
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules"]
}
```

该配置文件中包含以下特点：

*   `target`：编译目标为 ES2019。
*   `module`：输出模块为 CommonJS。
*   `lib`：使用 ES2019 标准库。
*   `outDir`：输出目录为 `dist`。
*   `rootDir`：源代码目录为 `src`。
*   `strict`：启用严格模式。
*   `esModuleInterop`：允许导入 CommonJS 模块。
*   `resolveJsonModule`：允许导入 JSON 文件。
*   `sourceMap`：生成 sourcemap。
*   `declaration`：生成类型声明文件。
*   `moduleResolution`：模块解析方式为 Node.js。
*   `noUnusedLocals`：禁止未使用的局部变量。
*   `noUnusedParameters`：禁止未使用的函数参数。
*   `strictNullChecks`：禁止 null 和 undefined 类型的赋值。
*   `noImplicitReturns`：函数必须显式返回类型。
*   `noImplicitThis`：禁止隐式的 this 类型。
*   `noImplicitAny`：允许隐式的 any 类型（因为在某些情况下 any 类型是必须的）。
*   `experimentalDecorators`：启用实验性装饰器。
*   `emitDecoratorMetadata`：启用装饰器元数据的生成。
*   `forceConsistentCasingInFileNames`：禁止大小写不一致的文件名。
*   `skipLibCheck`：跳过库文件的类型检查（加快编译速度）。

这份配置文件旨在提供一种保证代码质量和可维护性的方式，同时也允许一些常见的编程错误。但需要注意的是，具体的配置还需要根据项目的实际情况进行调整。