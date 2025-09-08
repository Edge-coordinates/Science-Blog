---
title: contract
date: 2025/7/21 6:0:12
categories:
  - - Framework
    - Backend
    - REST-and-GraphQL
abbrlink: e98f2859
---

學習Contract是一個美麗的過程，的確是很優秀的設計，這篇了了學習感悟。


## POST 設計
``` ts
createReaction: {
      method: "POST",
      path: "/objects/:objectType/:objectId/award",
      body: AwardSchema.omit({ id: true, createdAt: true, user: true }).extend({
          userId: z.string(), // pass current user id
      }),
      responses: { 201: AwardSchema },
  },
```
這是個 很標準的 RESTful API Endpoint 定義，我一開始對於使用`omit` (omit方法用於從一個schema中移除指定欄位)感到疑惑，解釋是這樣的  
掉 id、createdAt、user），這是因為這些欄位通常是由後端產生的，不該由用戶提交（比如 id 是資料庫產的，createdAt 是伺服器時間）.extend({ userId })：因為這筆資料屬於某個使用者，要標註「誰點的讚」或「誰給的反應」  