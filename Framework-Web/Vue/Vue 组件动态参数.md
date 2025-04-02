---
title: Vue 组件动态参数
date: 2025/3/29 19:31:30
categories:
  - - Framework-Web
    - Vue
  - Vue
abbrlink: 5d4bf2fe
---


## 动态属性

```vue
<MyCarousel v-bind="shouldAutoplay ? { autoplayInterval: 3000 } : {}" />
```

组合多个条件对象时，... 就会有用：

```vue
<MyCarousel v-bind="{
  ...baseProps,
  ...(shouldAutoplay ? { autoplayInterval: 3000 } : {}),
  ...(showArrows ? { showArrows: true } : {})
}" />

```


## 动态 Style

```vue
<template>
  <div :style="{ width: widthValue }" class="your-other-classes">
    <!-- 内容 -->
  </div>
</template>

<script setup lang="ts">
defineProps<{
  widthValue?: string
}>()
</script>

```