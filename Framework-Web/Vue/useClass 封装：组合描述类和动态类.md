---
title: useClass 封装：组合描述类和动态类
date: 2025/3/27 18:55:44
categories:
  - - Framework-Web
    - Vue
abbrlink: "58187742"
---
太好了！以下是一个通用且实用的 `useClass` 组合函数，它可以帮你把“**描述类**”和“**动画类/状态类**”清晰分开管理，并在模板中优雅地使用。

---

## ✅ `useClass` 封装：组合描述类和动态类

```ts
// composables/useClass.js
import { computed } from "vue";

/**
 * @param baseClass 静态基础类（字符串或字符串数组）
 * @param dynamicClasses 动态类对象 { 'class-name': true/false }
 * @returns Computed ref of full class string
 */
export function useClass(baseClass, dynamicClasses = {}) {
  return computed(() => {
    const base = Array.isArray(baseClass) ? baseClass : [baseClass];
    const dynamic = Object.entries(dynamicClasses)
      .filter(([, value]) => value)
      .map(([key]) => key);

    return [...base, ...dynamic].join(" ");
  });
}
```

---

## ✅ 使用示例（推荐搭配 Vue `<script setup>`）

```vue
<template>
  <div :class="boxClass">
    动画盒子
  </div>

  <button @click="toggle">切换动画</button>
</template>

<script setup>
import { ref } from "vue";
import { useClass } from "@/composables/useClass";

const isVisible = ref(true);

// 静态描述类 + 动态动画类
const boxClass = useClass("box bg-blue-200 p-4", {
  "animate-fade-in": isVisible,
  "animate-fade-out": !isVisible,
});

function toggle() {
  isVisible.value = !isVisible.value;
}
</script>

<style scoped>
/* 假设你有这两个动画类 */
.animate-fade-in {
  animation: fadeIn 0.5s ease-out forwards;
}
.animate-fade-out {
  animation: fadeOut 0.5s ease-in forwards;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeOut {
  from { opacity: 1; transform: translateY(0); }
  to { opacity: 0; transform: translateY(10px); }
}
</style>
```

---

## ✨ 优点

- ✅ 可读性高（结构类和动画类分离）
- ✅ 动态类切换灵活
- ✅ 可复用性强（`useClass()` 可用于多个组件）

---

如果你想让 `useClass` 支持 **响应式断点**、**合并多个动态组**、或配合 `@vueuse/motion` 等库用，我也可以写进高级版。

需要我扩展支持 Tailwind 的断点响应式判断（如 `isMobile` 自动加上 `sm:opacity-0`）吗？