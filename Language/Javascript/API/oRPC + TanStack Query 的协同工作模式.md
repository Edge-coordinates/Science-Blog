---
title: oRPC + TanStack Query 的协同工作模式
date: 2025/09/11 03:17:06
updated: 2025/09/11 03:19:47
categories:
  - - Language
    - Javascript
    - API
abbrlink: 15f9ab4d
---

# oRPC + TanStack Query 的协同工作模式

> https://orpc.unnoq.com/docs/integrations/tanstack-query

### 第一部分：oRPC 客户端的基础使用（不依赖任何请求库）

在不使用任何状态管理库的情况下，oRPC 客户端本身就是一个功能强大且类型安全的请求工具。

#### **步骤 1：创建客户端实例**

首先，您需要创建一个客户端实例。这个实例是您前端应用与后端 API 通信的唯一入口。您需要一个 "Link" 来告诉客户端如何与后端通信。

```typescript
// src/lib/orpcClient.ts
import { createORPCClient } from '@orpc/client';
import { RPCLink } from '@orpc/client/fetch'; // 假设后端使用 RPCHandler
// 如果后端是 OpenAPI，则使用 import { OpenAPILink } from '@orpc/openapi-client/fetch';

// 导入后端路由的类型定义，这是实现端到端类型安全的关键！
// 在 Monorepo 或共享包架构中，这非常容易实现。
import type { AppRouter } from '../../api-gateway/src/router'; // 假设这是您后端路由的类型
import type { RouterClient } from '@orpc/server';

const link = new RPCLink({
  url: 'http://localhost:3000/rpc', // 您的 API 网关地址
  // 您可以在这里配置全局的请求头，例如用于身份验证的 token
  headers: () => {
    const token = localStorage.getItem('token');
    if (token) {
      return {
        Authorization: `Bearer ${token}`,
      };
    }
    return {};
  },
});

// 创建客户端，并赋予它从后端推断出的完整类型
export const client: RouterClient<typeof AppRouter> = createORPCClient(link);
```

#### **步骤 2：发起请求**

创建客户端后，您就可以在代码的任何地方（例如 React/Vue 组件、或普通的业务逻辑文件中）发起请求了。整个过程就像调用一个本地的异步函数，并且拥有完美的自动补全和类型检查。

```typescript
import { client } from '../lib/orpcClient';

async function fetchPlanets() {
  try {
    // 就像调用一个本地函数一样
    // 1. 输入参数是完全类型安全的，IDE 会提示您需要哪些字段
    const planets = await client.planet.list({ limit: 10 });

    // 2. 返回的数据也是完全类型安全的，planets 的类型是 (Planet[])
    console.log(planets[0].name); // IDE 知道 planet 对象上有 name 字段

  } catch (error) {
    // 处理未知错误
    console.error("请求失败:", error);
  }
}
```

#### **步骤 3：错误处理 (`safe` 工具)**

为了避免到处写 `try/catch`，oRPC 提供了一个非常有用的 `safe` 工具函数，它可以将 Promise 的结果包装成一个元组 `[error, data]`。

```typescript
import { client } from '../lib/orpcClient';
import { safe, isDefinedError } from '@orpc/client';

async function createPlanet(name: string) {
  // safe 会捕获任何错误，并将其作为第一个元素返回
  const [error, newPlanet] = await safe(client.planet.create({ name }));

  if (error) {
    // 如果是后端在 .errors 中定义的、可预期的类型安全错误
    if (isDefinedError(error)) { //
      // error.data 的类型是完全安全的
      alert(`创建失败: ${error.message}, 原因: ${error.data.reason}`);
    } else {
      // 其他未知错误
      alert(`发生未知错误: ${error.message}`);
    }
    return;
  }

  // 请求成功
  console.log('新行星已创建:', newPlanet.id);
}
```

-----

### 第二部分：配合 TanStack Query - 现代前端数据请求的最佳实践

虽然 oRPC 的基础客户端很好用，但在现代前端应用中，我们需要的不仅仅是数据请求。我们还需要**服务器状态管理**，包括：

  * **缓存**：避免重复请求相同的数据。
  * **自动重新验证**：在用户切换窗口或网络重连时自动更新数据。
  * **加载与错误状态管理**：轻松获取 UI 所需的 `isLoading`, `isError` 等状态。
  * **修改与缓存失效**：在创建或更新数据后，能方便地让相关的查询缓存失效并重新获取。

这正是 TanStack Query 所做的。oRPC 与它进行了深度集成，让这一切变得极其简单。

#### **步骤 1：安装集成包**

```bash
pnpm add @orpc/tanstack-query @tanstack/react-query # 以 React 为例
```

#### **步骤 2：创建 oRPC Query 工具集 (`Utils`)**

这是连接 oRPC 和 TanStack Query 的桥梁。您需要用 oRPC 提供的工具函数来包装您之前创建的 `client` 实例。

```typescript
// src/lib/orpcQuery.ts
import { createTanstackQueryUtils } from '@orpc/tanstack-query';
import { client } from './orpcClient'; // 导入我们第一部分创建的 client

// 这个 orpc 对象现在被赋予了超能力
// 它里面的每个程序都多了 .queryOptions, .mutationOptions, .key 等方法
export const orpc = createTanstackQueryUtils(client);
```

#### **步骤 3：核心用法（以 React 为例）**

现在，您可以像使用原生的 TanStack Query 一样，但是 oRPC 集成包会为您自动处理掉最繁琐的部分（`queryKey` 和 `queryFn`）。

**A. 查询数据 (`useQuery`)**

```tsx
import { useQuery } from '@tanstack/react-query';
import { orpc } from '../lib/orpcQuery';

function PlanetList() {
  const { data, isLoading, isError } = useQuery(
    // oRPC 的魔法：.queryOptions 会自动为您生成类型安全的 queryKey 和 queryFn！
    // 您再也不用手动拼写 queryKey，也不用写 (context) => client.planet.list() 了
    orpc.planet.list.queryOptions({ input: { limit: 10 } }) //
  );

  if (isLoading) return <div>正在加载...</div>;
  if (isError) return <div>加载失败！</div>;

  return (
    <ul>
      {data.map(planet => <li key={planet.id}>{planet.name}</li>)}
    </ul>
  );
}
```

**B. 修改数据 (`useMutation`)**

```tsx
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { orpc } from '../lib/orpcQuery';

function CreatePlanetForm() {
  const queryClient = useQueryClient();

  const mutation = useMutation(
    // .mutationOptions 同样会自动生成 mutationFn
    orpc.planet.create.mutationOptions({
      // TanStack Query 的标准功能：修改成功后...
      onSuccess: () => {
        // ...让 "planet list" 这个查询缓存失效，从而触发自动重新获取
        queryClient.invalidateQueries({
          // oRPC 的魔法：.key() 方法可以精准地生成需要失效的 queryKey
          queryKey: orpc.planet.list.key(),
        });
      },
    })
  );

  const handleSubmit = (event) => {
    event.preventDefault();
    const name = new FormData(event.target).get('name') as string;
    // 调用 mutation，输入参数是完全类型安全的
    mutation.mutate({ name });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" disabled={mutation.isPending} />
      <button type="submit" disabled={mutation.isPending}>
        {mutation.isPending ? '创建中...' : '创建行星'}
      </button>
    </form>
  );
}
```

**C. 无限滚动 (`useInfiniteQuery`)**

```tsx
import { useInfiniteQuery } from '@tanstack/react-query';
import { orpc } from '../lib/orpcQuery';

function InfinitePlanetList() {
  const {
    data,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage
  } = useInfiniteQuery(
    // .infiniteOptions 帮助您配置无限滚动
    orpc.planet.listWithCursor.infiniteOptions({
      // input 必须是一个接收 pageParam 的函数
      input: (pageParam) => ({ cursor: pageParam }), //
      initialPageParam: 0, // 初始页的 cursor
      // 告诉 TanStack Query 如何从上一页数据中获取下一页的 cursor
      getNextPageParam: (lastPage) => lastPage.nextCursor,
    })
  );

  // ... UI 渲染逻辑 ...
}
```

### 总结：oRPC + TanStack Query 的协同工作模式

您可以这样理解它们的关系：

  * **oRPC Client (`client`)**：是**类型安全的管道工**。它负责建立从前端到后端的、数据类型完全正确的通信管道。
  * **TanStack Query**：是**智能的水库和调度中心**。它决定了什么时候通过管道取水（发起请求）、取来的水（数据）要缓存多久、什么时候水变质了需要重新取（缓存失效和重新验证）。
  * **`@orpc/tanstack-query` (`orpc` a.k.a. Utils)**：是**管道工和调度中心的“智能适配器”**。它将 oRPC 的类型安全能力无缝对接给 TanStack Query，自动完成了所有繁琐的配置工作，让您可以专注于业务逻辑，同时享受两个库带来的最大优势。