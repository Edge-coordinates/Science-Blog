---
title: Scrapy 入门教程
categories:
  - Python
tags:
  - Scrapy
reprint: true
abbrlink: b2c7d74
---



> 转载自[Scrapy 入门教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/w3cnote/scrapy-detail.html)


Scrapy 是用 Python 实现的一个为了爬取网站数据、提取结构性数据而编写的应用框架。

Scrapy 常应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。

通常我们可以很简单的通过 Scrapy 框架实现一个爬虫，抓取指定网站的内容或图片。

* * *

Scrapy 架构图 (绿线是数据流向)
--------------------

![](https://www.runoob.com/wp-content/uploads/2018/10/8c591d54457bb033812a2b0364011e9c_articlex.png)

*   **Scrapy Engine(引擎)**: 负责 Spider、ItemPipeline、Downloader、Scheduler 中间的通讯，信号、数据传递等。
    
*   **Scheduler(调度器)**: 它负责接受引擎发送过来的 Request 请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎。
    
*   **Downloader（下载器）**：负责下载 Scrapy Engine(引擎) 发送的所有 Requests 请求，并将其获取到的 Responses 交还给 Scrapy Engine(引擎)，由引擎交给 Spider 来处理，
    
*   **Spider（爬虫）**：它负责处理所有 Responses, 从中分析提取数据，获取 Item 字段需要的数据，并将需要跟进的 URL 提交给引擎，再次进入 Scheduler(调度器).
    
*   **Item Pipeline(管道)**：它负责处理 Spider 中获取到的 Item，并进行进行后期处理（详细分析、过滤、存储等）的地方。
    
*   **Downloader Middlewares（下载中间件）**：你可以当作是一个可以自定义扩展下载功能的组件。
    
*   **Spider Middlewares（Spider 中间件）**：你可以理解为是一个可以自定扩展和操作引擎和 Spider 中间通信的功能组件（比如进入 Spider 的 Responses; 和从 Spider 出去的 Requests）
    

Scrapy 的运作流程
------------

代码写好，程序开始运行...

*   1 引擎：Hi！Spider, 你要处理哪一个网站？
*   2 Spider：老大要我处理 xxxx.com。
*   3 引擎：你把第一个需要处理的 URL 给我吧。
*   4 Spider：给你，第一个 URL 是 xxxxxxx.com。
*   5 引擎：Hi！调度器，我这有 request 请求你帮我排序入队一下。
*   6 调度器：好的，正在处理你等一下。
*   7 引擎：Hi！调度器，把你处理好的 request 请求给我。
*   8 调度器：给你，这是我处理好的 request
*   9 引擎：Hi！下载器，你按照老大的下载中间件的设置帮我下载一下这个 request 请求
*   10 下载器：好的！给你，这是下载好的东西。（如果失败：sorry，这个 request 下载失败了。然后引擎告诉调度器，这个 request 下载失败了，你记录一下，我们待会儿再下载）
*   11 引擎：Hi！Spider，这是下载好的东西，并且已经按照老大的下载中间件处理过了，你自己处理一下（注意！这儿 responses 默认是交给 def parse() 这个函数处理的）
*   12 Spider：（处理完毕数据之后对于需要跟进的 URL），Hi！引擎，我这里有两个结果，这个是我需要跟进的 URL，还有这个是我获取到的 Item 数据。
*   13 引擎：Hi ！管道 我这儿有个 item 你帮我处理一下！调度器！这是需要跟进 URL 你帮我处理下。然后从第四步开始循环，直到获取完老大需要全部信息。
*   14 管道调度器：好的，现在就做！

**注意！只有当调度器中不存在任何 request 了，整个程序才会停止，（也就是说，对于下载失败的 URL，Scrapy 也会重新下载。）**

* * *

制作 Scrapy 爬虫 一共需要 4 步：
----------------------

1.  新建项目 (scrapy startproject xxx)：新建一个新的爬虫项目
2.  明确目标 （编写 items.py）：明确你想要抓取的目标
3.  制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页
4.  存储内容 （pipelines.py）：设计管道存储爬取内容

* * *

安装
--

### Windows 安装方式

升级 pip 版本：

```
pip install --upgrade pip
```

通过 pip 安装 Scrapy 框架:

```
pip install Scrapy
```

### Ubuntu 安装方式

安装非 Python 的依赖:

```
sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

通过 pip 安装 Scrapy 框架：

```
sudo pip install scrapy
```

### Mac OS 安装方式

对于 Mac OS 系统来说，由于系统本身会引用自带的 python2.x 的库，因此默认安装的包是不能被删除的，但是你用 python2.x 来安装 Scrapy 会报错，用 python3.x 来安装也是报错，我最终没有找到直接安装 Scrapy 的方法，所以我用另一种安装方式来说一下安装步骤，解决的方式是就是使用 virtualenv 来安装。

```
$ sudo pip install virtualenv
$ virtualenv scrapyenv
$ cd scrapyenv
$ source bin/activate
$ pip install Scrapy
```

安装后，只要在命令终端输入 scrapy，提示类似以下结果，代表已经安装成功。

![](https://www.runoob.com/wp-content/uploads/2018/10/3748346984-5a79c47d84aba_articlex.png)

* * *

入门案例
----

### 学习目标

*   创建一个 Scrapy 项目
*   定义提取的结构化数据 (Item)
*   编写爬取网站的 Spider 并提取出结构化数据 (Item)
*   编写 Item Pipelines 来存储提取到的 Item(即结构化数据)

### 一. 新建项目 (scrapy startproject)

在开始爬取之前，必须创建一个新的 Scrapy 项目。进入自定义的项目目录中，运行下列命令：

```
scrapy startproject mySpider
```

其中， mySpider 为项目名称，可以看到将会创建一个 mySpider 文件夹，目录结构大致如下：

下面来简单介绍一下各个主要文件的作用：

```
mySpider/
    scrapy.cfg
    mySpider/
        __init__.py
        items.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
            ...
```

这些文件分别是:

*   scrapy.cfg: 项目的配置文件。
*   mySpider/: 项目的 Python 模块，将会从这里引用代码。
*   mySpider/items.py: 项目的目标文件。
*   mySpider/pipelines.py: 项目的管道文件。
*   mySpider/settings.py: 项目的设置文件。
*   mySpider/spiders/: 存储爬虫代码目录。

### 二、明确目标 (mySpider/items.py)

我们打算抓取 **http://www.itcast.cn/channel/teacher.shtml** 网站里的所有讲师的姓名、职称和个人信息。

1.  打开 mySpider 目录下的 items.py。
    
2.  Item 定义结构化数据字段，用来保存爬取到的数据，有点像 Python 中的 dict，但是提供了一些额外的保护减少错误。
    
3.  可以通过创建一个 scrapy.Item 类， 并且定义类型为 scrapy.Field 的类属性来定义一个 Item（可以理解成类似于 ORM 的映射关系）。
    

接下来，创建一个 ItcastItem 类，和构建 item 模型（model）。

```python
import scrapy

class ItcastItem(scrapy.Item):
   name = scrapy.Field()
   title = scrapy.Field()
   info = scrapy.Field()
```

### 三、制作爬虫 （spiders/itcastSpider.py）

爬虫功能要分两步：

**1. 爬数据**

在当前目录下输入命令，将在 mySpider/spider 目录下创建一个名为 itcast 的爬虫，并指定爬取域的范围：

```
scrapy genspider itcast "itcast.cn"
```

打开 mySpider/spider 目录里的 itcast.py，默认增加了下列代码:

```python
import scrapy

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = (
        'http://www.itcast.cn/',
    )

    def parse(self, response):
        pass
```

其实也可以由我们自行创建 itcast.py 并编写上面的代码，只不过使用命令可以免去编写固定代码的麻烦

要建立一个 Spider， 你必须用 scrapy.Spider 类创建一个子类，并确定了三个强制的属性 和 一个方法。

name = "" ：这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。

allow_domains = [] 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的 URL 会被忽略。

start_urls = () ：爬取的 URL 元祖 / 列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些 urls 开始。其他子 URL 将会从这些起始 URL 中继承性生成。

parse(self, response) ：解析的方法，每个初始 URL 完成下载后将被调用，调用的时候传入从每一个 URL 传回的 Response 对象来作为唯一参数，主要作用如下：

负责解析返回的网页数据 (response.body)，提取结构化数据 (生成 item)  
生成需要下一页的 URL 请求。  
将 start_urls 的值修改为需要爬取的第一个 url

```
start_urls = ("http://www.itcast.cn/channel/teacher.shtml",)
```

修改 parse() 方法

```python
def parse(self, response):
    filename = "teacher.html"
    open(filename, 'w').write(response.body)
```

然后运行一下看看，在 mySpider 目录下执行：

```
scrapy crawl itcast
```

是的，就是 itcast，看上面代码，它是 ItcastSpider 类的 name 属性，也就是使用 scrapy genspider 命令的唯一爬虫名。

运行之后，如果打印的日志出现 [scrapy] INFO: Spider closed (finished)，代表执行完成。 之后当前文件夹中就出现了一个 teacher.html 文件，里面就是我们刚刚要爬取的网页的全部源代码信息。

**注意:** Python2.x 默认编码环境是 ASCII，当和取回的数据编码格式不一致时，可能会造成乱码；我们可以指定保存内容的编码格式，一般情况下，我们可以在代码最上方添加

```python
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
```

这三行代码是 Python2.x 里解决中文编码的万能钥匙，经过这么多年的吐槽后 Python3 学乖了，默认编码是 Unicode 了...(祝大家早日拥抱 Python3)

**2. 取数据**

爬取整个网页完毕，接下来的就是的取过程了，首先观察页面源码：

```html
<div>
    <h3>  xxx  </h3>
    <h4> xxxxx </h4>
    <p> xxxxxxxx </p>
```

是不是一目了然？直接上 XPath 开始提取数据吧。

xpath 方法，我们只需要输入的 xpath 规则就可以定位到相应 html 标签节点，详细内容可以查看 [xpath 教程](https://www.runoob.com/xpath/xpath-tutorial.html)。

不会 xpath 语法没关系，Chrome 给我们提供了一键获取 xpath 地址的方法（**右键 -> 检查 ->copy->copy xpath**）, 如下图:

![](https://www.runoob.com/wp-content/uploads/2018/10/xpath-chrome.jpg)

这里给出一些 XPath 表达式的例子及对应的含义:

*   `/html/head/title`: 选择 HTML 文档中 `<head>` 标签内的 `<title>` 元素
*   `/html/head/title/text()`: 选择上面提到的 `<title>` 元素的文字
*   `//td`: 选择所有的 `<td>` 元素
*   `//div[@class="mine"]`: 选择所有具有 `class="mine"` 属性的 `div` 元素

举例我们读取网站 **http://www.itcast.cn/** 的网站标题，修改 itcast.py 文件代码如下：：

```python
# -*- coding: utf-8 -*-
import scrapy

# 以下三行是在 Python2.x版本中解决乱码问题，Python3.x 版本的可以去掉
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Opp2Spider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.com']
    start_urls = ['http://www.itcast.cn/']

    def parse(self, response):
        # 获取网站标题
        context = response.xpath('/html/head/title/text()')   
       
        # 提取网站标题
        title = context.extract_first()  
        print(title) 
        pass
```

执行以下命令：

```
$ scrapy crawl itcast
...
...
传智播客官网-好口碑IT培训机构,一样的教育,不一样的品质
...
...
```

我们之前在 mySpider/items.py 里定义了一个 ItcastItem 类。 这里引入进来:

```Python
from mySpider.items import ItcastItem
```

然后将我们得到的数据封装到一个 ItcastItem 对象中，可以保存每个老师的属性：

```python
from mySpider.items import ItcastItem

def parse(self, response):
    #open("teacher.html","wb").write(response.body).close()

    # 存放老师信息的集合
    items = []

    for each in response.xpath("//div[@class='li_txt']"):
        # 将我们得到的数据封装到一个 `ItcastItem` 对象
        item = ItcastItem()
        #extract()方法返回的都是unicode字符串
        name = each.xpath("h3/text()").extract()
        title = each.xpath("h4/text()").extract()
        info = each.xpath("p/text()").extract()

        #xpath返回的是包含一个元素的列表
        item['name'] = name[0]
        item['title'] = title[0]
        item['info'] = info[0]

        items.append(item)

    # 直接返回最后数据
    return items
```

我们暂时先不处理管道，后面会详细介绍。

### 保存数据

scrapy 保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，命令如下：

```
scrapy crawl itcast -o teachers.json
```

json lines 格式，默认为 Unicode 编码

```
scrapy crawl itcast -o teachers.jsonl
```

csv 逗号表达式，可用 Excel 打开

```
scrapy crawl itcast -o teachers.csv
```

xml 格式

```
scrapy crawl itcast -o teachers.xml
```

### 思考

如果将代码改成下面形式，结果完全一样。

请思考 yield 在这里的作用 ([Python yield 使用浅析](https://www.runoob.com/w3cnote/python-yield-used-analysis.html))：

```python
# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem

# 以下三行是在 Python2.x版本中解决乱码问题，Python3.x 版本的可以去掉
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Opp2Spider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.com']
    start_urls = ("http://www.itcast.cn/channel/teacher.shtml",)

    def parse(self, response):
        #open("teacher.html","wb").write(response.body).close()

        # 存放老师信息的集合
        items = []

        for each in response.xpath("//div[@class='li_txt']"):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = ItcastItem()
            #extract()方法返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            #xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            items.append(item)

        # 直接返回最后数据
        return items
```

