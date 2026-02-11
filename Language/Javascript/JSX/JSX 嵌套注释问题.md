---
title: JSX 嵌套注释问题
date: 2026/02/11 23:57:22
categories:
  - - Language
    - Javascript
    - JSX
abbrlink: 480c8559
---
开发中需要面对嵌套注释问题由来已久，向来不知道应该怎么处理这样的问题，现在发现两个解决方案

## “原生”嵌套注释

```
<div>
    {/* This is the outer comment */}
    {
    // {/* The inner comment and surrounding JSX are effectively commented out here */}
    // <SomeComponent prop1="value" />
    // {/* Another inner comment */}
    }
</div>
```

## Nested Comments

[Market Link](https://marketplace.visualstudio.com/items?itemName=philsinatra.nested-comments)

[GitHub Link](https://github.com/philsinatra/NestedCommentsVSCode)

对了，这个插件cursor版本不支持，所以可以阅读[Cursor如何安装离线插件](../../../Environment/IDE/VSCode/Cursor如何安装离线插件.md)

Default Keybindings
- Mac: `cmd` + `alt` + `/`
- Windows: `ctrl` + `alt` + `/`

应该说对于这个插件算不上特别满意，比如需要单独的快捷键，比如必须完整的选择想要注释的内容（按行选择是不受支持的qwq）

其实需要单独的快捷键是可以理解的啦，毕竟嗯，所以vsc官方能不能出面解决这个问题呀！

效果:

```
{/*<div className="flex flex-1">
  /~ /~ Middle horizontal layout: Sidebar + Page Content ~/
  <Sidebar
    sidebarOpen={sidebarOpen}
    sidebarWidth={drawerWidth}
    sidebarHeaderClassName="mx-6"
    isMobile={isMobile}
    onClose={() => isMobile && closeSidebar()}
    handleDrawerToggle={toggleSidebar}
    NAVIGATION={NAVIGATION(isAdmin)}
  />~/
  <main className="flex flex-col flex-1 pt-[56px] sm:pt-[64px] transition-all duration-300 h-screen w-full">
    <div className="flex-1 pb-4 dark:bg-dark bg-light">{children}</div>
    <MainLayoutFooter />
  </main>
</div>*/}
```

这是两层嵌套，实际测试就是不能正常还原的了（注释是没问题的），不过如果只有一层

```
<div className="flex flex-1">
  {/* Middle horizontal layout: Sidebar + Page Content */}
  <Sidebar
    sidebarOpen={sidebarOpen}
    sidebarWidth={drawerWidth}
    sidebarHeaderClassName="mx-6"
    isMobile={isMobile}
    onClose={() => isMobile && closeSidebar()}
    handleDrawerToggle={toggleSidebar}
    NAVIGATION={NAVIGATION(isAdmin)}
  />
  <main className="flex flex-col flex-1 pt-[56px] sm:pt-[64px] transition-all duration-300 h-screen w-full">
    <div className="flex-1 pb-4 dark:bg-dark bg-light">{children}</div>
    <MainLayoutFooter />
  </main>
</div>
```

那么注释和还原都可以正常运行，实际上一般调试也都够用。

不过吾辈还是期待上文提到的“原生”嵌套注释，感觉可以支持多层嵌套哦。