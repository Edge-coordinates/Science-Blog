---
title: Elysia validation Error
date: 2025/11/05 16:58:48
categories:
  - - Framework
    - Web
    - Elysia
abbrlink: 20dc8b62
---
# Elysia validation Error

```
Type 'TObject<{ q: TOptional<TString>; tag: TOptional<TString>; tags: TOptional<TString>; authorId: TOptional<TString>; ... 4 more ...; limit: TOptional<...>; }>' is not assignable to type 'AnySchema | undefined'.
  Property ''~standard'' is missing in type 'TObject<{ q: TOptional<TString>; tag: TOptional<TString>; tags: TOptional<TString>; authorId: TOptional<TString>; ... 4 more ...; limit: TOptional<...>; }>' but required in type 'StandardSchemaV1Like<unknown, unknown>'.
```

可能的问题：

进入contract目录重新 bun install 

确保这两个包都在

reload window

反正，这个问题是可以解决的

```
"@sinclair/typebox": "^0.34.41",
"elysia": "^1.4.12"
```