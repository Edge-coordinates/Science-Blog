---
title: Vue 组件动画效果
date: '2025/3/27 18:55:44'
categories:
  - - Framework-Web
    - Vue
  - Vue
abbrlink: ac878bb1
---
#### You:
有没有什么库可以实现组件变幻 的动画效果比如淡入淡出

#### ChatGPT:
当然有！如果你想要在 Vue 项目中实现组件的**淡入淡出、滑动、缩放等动画过渡效果**，有几个非常推荐的方式或库可以实现，简单又漂亮👇

---

## ✅ 方式一：Vue 内建 `<Transition>`（最简）

Vue 自带的 `<Transition>` 组件就支持基本动画，比如淡入淡出：

```vue
<template>
  <button @click="show = !show">切换</button>
  <Transition name="fade">
    <div v-if="show" class="p-4 bg-blue-200">Hello</div>
  </Transition>
</template>

<script setup>
import { ref } from "vue";
const show = ref(true);
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
```

---

## ✅ 方式二：使用 Tailwind CSS 的动画类（简单强大）

如果你已经用了 Tailwind，可以搭配 `transition`, `duration`, `opacity`, `transform` 等类：

```vue
<template>
  <button @click="show = !show">切换</button>
  <div
    v-if="show"
    class="transition-opacity duration-500 ease-in-out opacity-100"
    :class="{ 'opacity-0': !show }"
  >
    Hello with Tailwind
  </div>
</template>
```

---

## ✅ 方式三：使用 VueUse 的动画类（组合式动画工具）

如果你用组合式 API 并喜欢封装好的 hooks，可以考虑 [VueUse](https://vueuse.org/) 提供的一些工具，比如 `useTransition()`。

---

## ✅ 方式四：使用 `motion` 动画库（更酷的动效）

[`@vueuse/motion`](https://motion.vueuse.org/) 是基于 [Popmotion](https://popmotion.io/) 的 Vue 动画库，写法类似 `Framer Motion`（React）：

```bash
npm install @vueuse/motion
```

```vue
<script setup>
import { useMotion } from '@vueuse/motion';
import { ref } from 'vue';

const show = ref(true);
</script>

<template>
  <button @click="show = !show">切换</button>

  <motion
    v-if="show"
    :initial="{ opacity: 0, y: -20 }"
    :enter="{ opacity: 1, y: 0 }"
    :leave="{ opacity: 0, y: 20 }"
    class="p-4 bg-green-200"
  >
    动画组件
  </motion>
</template>
```

✅ 优点：

- 支持 spring 弹簧动画
- 支持拖拽、缩放、滑动等高级交互
- 和 Vue 完美结合

---

## ✅ 总结推荐

| 需求               | 推荐方案                  |
| ---------------- | --------------------- |
| 简单淡入淡出           | Vue 内建 `<Transition>` |
| 快速 + Tailwind 样式 | Tailwind transition 类 |
| 想要高级动效           | `@vueuse/motion`      |

---

你想让多个组件切换时有不同动画？比如滑入/滑出或缩放？我可以帮你写一个完整切换动画容器组件～要不要？
