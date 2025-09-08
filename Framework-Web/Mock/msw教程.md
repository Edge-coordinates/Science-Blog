---
title: msw教程
date: 2025/7/1 21:25:28
categories:
  - - Framework-Web
    - Mock
abbrlink: e99f5e36
---


```powershell
pnpm add -D @graphql-codegen/cli @graphql-codegen/typescript @graphql-codegen/typescript-msw @graphql-codegen/typescript-operations msw @graphql-tools/utils
```

```powershell
pnpm add @urql/vue graphql graphql-tag

pnpm add graphql graphql-tag
```

1. Ensure mockServiceWorker.js is in your public directory.
```
npx msw init public/
```

`codegen.ts`

```ts
// codegen.ts
import type { CodegenConfig } from "@graphql-codegen/cli";

const config: CodegenConfig = {
  schema: "./src/mocks/schema.graphql",
  documents: ["src/graphql/**/*.ts"], // 你的 gql 查询语句位置
  generates: {
    "./src/graphql/generated.ts": {
      plugins: [
        "typescript", // 生成基础类型
        "typescript-operations", // 针对 operation 生成变量、返回值类型
        "typescript-msw", // 生成 MSW 支持的 GraphQL 文档（如 GetBooksDocument）
      ],
    },
  },
  overwrite: true,
  emitLegacyCommonJSImports: false,
};

export default config;
```

