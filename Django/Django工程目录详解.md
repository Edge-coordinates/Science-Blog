---
title: Django工程目录详解
categories:
- Django
tags:
---


作为一个新手,Django的目录结构还是经常让我搞混,下面做一个介介绍
```python
mysite/ # 外层容器，可以随意重命名
    manage.py # 管理 Django 项目的命令行工具
    mysite/ # 一个纯 Python 包，包含你的项目
        __init__.py
        settings.py
        urls.py   
        asgi.py
        wsgi.py
    polls/ # 通过 python manage.py startapp polls 创建的一个应用程序
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
        urls.py # 编写URLconf
        templates/ # 用于保存模板 或者有另一种建立方法，见下文
            polls/ # 因为不知名原因，必须创建一个与该应用程序同名的文件夹
                base.html # 你的模板文件
```

这些目录和文件的用处是：

*   最外层的 `mysite/` 根目录只是你项目的容器， 根目录名称对 Django 没有影响，你可以将它重命名为任何你喜欢的名称。

*   `manage.py`: 一个让你用各种方式管理 Django 项目的命令行工具。你可以阅读 [django-admin 和 manage.py](../../ref/django-admin/) 获取所有 `manage.py` 的细节。

*   里面一层的 `mysite/` 目录包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 `mysite.urls`).

*   `mysite/__init__.py`：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果你是 Python 初学者，阅读官方文档中的 [更多关于包的知识](https://docs.python.org/3/tutorial/modules.html#tut-packages "(在 Python v3.10)")。

*   `mysite/settings.py`：Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看 [Django 配置](../../topics/settings/) 了解细节。

*   `mysite/urls.py`：Django 项目的 URL 声明，就像你网站的 “目录”。阅读 [URL 调度器](../../topics/http/urls/) 文档来获取更多关于 URL 的内容。

*   `mysite/asgi.py`：作为你的项目的运行在 ASGI 兼容的 Web 服务器上的入口。阅读 [如何使用 ASGI 来部署](../../howto/deployment/asgi/) 了解更多细节。

*   `mysite/wsgi.py`：作为你的项目的运行在 WSGI 兼容的 Web 服务器上的入口。阅读 [如何使用 WSGI 进行部署](../../howto/deployment/wsgi/) 了解更多细节。

## 注释
- `polls/templates`文件夹可以移到项目的根目录下，即外层的mysite目录下。这需要修改项目的settings.py文件，即内层mysite文件夹下的settings.py文件。在其中找到下方代码并更改，并在文件头部引入os库， `import os`。
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [], # 这是原来的
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # 改为使用这个
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
