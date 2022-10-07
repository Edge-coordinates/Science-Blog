**一、概念**

*   Node.js 不是语言、不是库、不是框架；
*   Node.js 是 JavaScript 的运行环境，可以解析、执行 JavaScript 代码；
*   使 JavaScript 可以脱离浏览器来运行；

**二、组成部分**  
1、浏览器中 JavaScript：

*   ECMAScript
*   DOM
*   BOM

2、[Node](https://so.csdn.net/so/search?q=Node&spm=1001.2101.3001.7020).js 中 JavaScript：

*   ECMAScript
*   没有 DOM、BOM
*   为 JavaScript 提供了一些服务器级别的操作 API：
    *   文件读写
    *   网络服务的构建
    *   网络通信
    *   http 服务器等。。。

**三、特点**

*   事件驱动
*   非阻塞 IO 模型（异步）
*   轻量和高效
*   构建于 chrome 的 V8 引擎 之上

**四、用途**

*   web 后台服务器
*   命令行工具

**五、主要知识点**

*   B/S 编程模型
*   模块化编程
*   Node 常用 API
*   异步编程
*   Express 开发框架
*   Ecmascript 6

**六、安装使用**

*   [官网下载](https://nodejs.org/en/)：稳定版（LTS）、最新体验版（Current）；（重复下载会升级覆盖）
*   命令行检查：`node --version/node -v`；
*   对应目录下执行 js 脚本文件：`node aa.js`
    *   创建 JavaScript 脚本文件，不要使用`node.js`
    *   打开命令行工具定位到文件
    *   执行 js 文件
*   **读写文件：fs 模块（file-system 文件系统：提供所有文件操作 API）**
    *   引入模块：`var fs = require('fs')`
    *   读文件：`fs.readFile('文件路径',回调函数function(error,data){ if(error){ console.log('友好地提示：读取失败') } else{ console.log(data)} })`，
        *   读取成功：（data：所读数据；error：null）
        *   读取失败：（data：null；error：错误对象 (直接展示给用户不友好)）
        *   默认返回二进制数据（以十六进制显示），使用`toString()`；
        *   例如：`fs.readFile('./hello.txt',function(error,data){ console.log(data.toString())})`
    *   写文件：`fs.writeFile('文件路径',‘文件内容’,回调函数function(error){})`
        *   写入成功：error：null，
        *   写入失败：error：错误对象
    *   删除、创建文件等。。。
*   **http 服务：http 模块**
    *   请求、响应都在实例的`on`方法的回调函数中；
    *   请求：主要用于告诉服务器，客户端传的是什么路径；`req.url`
    *   响应：用于针对不同路径做对应响应，只能传字符串或二进制（读取文件时的数据就是二进制），所以其他数据需要转成字符串 / 二进制；
        *   方式一：`res.write([响应内容]);res.end();`
        *   方式二：直接`res.end([响应内容])；`
    *   响应内容：必须是字符串（通过编码规则转成二进制）或二进制，因为在前后端不同语言间传输的数据是以 JSON 字符串形式；
        *   `JSON.stringify();`转成 json 字符串（序列化：用于传输）；

```
var http = require('http')
var server = http.createServer()//返回一个实例
server.on('request',function(request,response){
	console.log('当前访问的路径是'+ request.url)
	//这行代码时展示在服务器上的；url是端口号后面的部分，默认`/`根路径
	var url = req.url;
	if(url == '/'){
		response.end('hello 首页');//中文会有乱码，要配置响应内容类型
	}
	else{
		response.setHeader('Content-Type','text/plain;charset=utf-8');
		//告诉浏览器响应数据类型为普通文本，字符编码格式是utf-8；
		response.write('hello 其他');
		//中文会有乱码，要配置响应内容类型
		response.end();
	}
	//响应到客户端页面中，end()方法表示响应结束，否则浏览器一直等待。
})
//监听客户端打开网址，服务器收到请求时回调
server.listen(3000,function(){
	console.log('服务器启动成功了，可以通过 http://127.0.0.1:3000/ 来进行访问！')
})
//当服务启动后回调,80端口时客户端不需要输端口；
```

**七、Node 中的 JavaScript**

*   EcmaScript
*   内置的具名的[核心模块](http://nodejs.cn/api/)：`var [模块名] = require('[模块名]')`；
    *   常用：`fs,http,os,path,`
*   第三方模块：`Express`web 开发框架，需要下载引用；
*   用户自定义模块：就是常说的**模块化**编程，引入 js 文件；
    *   Node 中没有全局作用域，只有模块作用域，即引入的不同 js 文件，不能互相访问内部变量；所以要在 js 文件内使用`exports`对象导出内部变量、方法；
    *   引入时可以不写后缀`.js`；但必须写相对路径`./,../`，否则会被认为是核心模块，报错！

**八、服务器端的 ip 与端口号**

*   IP：ip 地址用来定位计算机；
*   端口号：0~65536，端口号用于定位具体的应用程序；（因为一台计算机有多个应用程序，靠 IP 地址无法区分通讯）
    *   客户端中浏览器等应用程序会默认找一个空闲端口来与服务器通信；
    *   一些指定端口号与指定服务联系，不会被默认使用；
    *   80 端口号，一般在上线部署时用，浏览器默认加 80，用户就不用写了；
    *   3000 端口号，一般在开发测试时用；
*   所有需要联网通信的应用程序都会占用一个端口号；
*   互相通信的计算机都知道彼此 IP 地址、端口号；
*   所以一台服务器可以开启多个服务，每个服务对应一个端口号。

**九、响应内容类型**

> **问题原因：**  
> 服务器默认发送的 json 字符串数据（读取文件时文件内容编码成的二进制所采用的规则由文件创建时的编码环境决定, 一般用开发工具创建的文件都是 utf-8）就是`utf-8`编码，但是浏览器默认不知道是什么编码，会按当前操作系统默认的编码格式，如：中文操作系统的默认编码规则：`GBK`，两者规则不同导致中文乱码。  
> （对于直接传二进制数据流时，因为不同编码规则对数字、字母的编码都一样，在通过二进制解码 html 文件前部分字母是都很正常，中文操作系统用`GBK`正常解码二进制数据，识别看到`meta`便知道用`UTF-8`，所以在传 html 文件时要声明类型和编码规则，元数据`meta`中定义的编码格式等同于在服务器端响应编码格式）

> **解决方案：**  
> 声明响应数据的类型（普通文本`text/plain`、html 代码`text/html`等），并告诉浏览器编码格式`charset=utf-8`；  
> 不管以字符串形式还是二进制传的都可以视情况需要在服务器设置响应数据类型：提供数据类型和编码格式给浏览器

> **发送的数据与对应响应类型：**  
> [Content-Type 对照表](https://tool.oschina.net/commons/)
> 
> *   图片需要指定响应类型，但不需要指定编码格式；
> *   一般只为字符数据（中文、字母、数字、符号等）指定编码格式 `utf-8`；  
>     如：`res.setHeader('Content-Type','text/plain;charset = utf-8')`  
>     如：`res.setHeader('Content-Type','text/html;charset = utf-8')`
> *   **特别地**：对于响应读取 html 文件的内容时，可以不写上述声明是因为浏览器自动识别 html 代码，并且 html 代码中`meta元数据`也可以声明编码格式。  
>     

**十、代码书写风格与分号的使用**

**常见代码书写风格规范：**

*   [JavaScript Standard Style 标准风格](https://standardjs.com/)
*   [Airbnb JavaScript Style](https://github.com/airbnb/javascript)

**一般推荐不加分号，必须加分号的情况：**

*   以模板字符串` `` `开头的代码前加`;`
*   以`()`开头的代码前加`;()`
*   以`[]`开头的代码前加`;[]`

**十一、node.js 实现 Apache 功能**

1、实现浏览器输入域名 + 端口号 / 文件名，就显示服务器上指定文件对应的内容；

*   利用`if语句`判断用户输入的路径；
*   利用`fs`模块，针对不同路径找到对应文件并读取内容（可以直接响应，因为`fs.readFile()`默认返回的`data`就是二进制（以十六进制显示），如果要对`data`进行处理可以`toString()`转为字符串）；

2、实现在浏览器显示文件目录功能；

*   利用`http`核心模块创建服务；
*   利用`fs.readdir(path[, options], callback)`核心模块读取文件目录信息，返回数组形式，用于模板引擎替换目录数据；
*   怎么替换？：要使用模板引擎内置方法：`{{each [数组名]}} <p>数组中的{{$value}}</p> {{/each}}`，遍历数组中每一项从而生产每一项
*   利用`fs.readFile(path[, options], callback)`核心模块读取用于目录显示的 html 模板文件并结合模板引擎`如：art-template`第三方模块替换目录内容（所以要`data.toString()`将二进制先转为字符串，当做替换模板使用）；
*   重点：怎么判断目录是文件夹还是文件？也有模块可以实现；
*   最终将改好的字符串响应给浏览器`res.end(newData)`，实现在浏览器显示目录、点击目录。

> 补充：第三方`art-template`模板引擎规则是识别字符串内`{{}}`中的变量名；（可在前端 html 页面中使用，也可以在后端 node 中安装使用）  
> 补充：在`Node`中使用方式：

```
var template = require('art-tmplate')
var ret = template.render(data.toString(),{name:'jack'})
//改后的新字符串
```

**十二、客户端渲染与服务端渲染**

*   渲染：就是将数据以 html 元素这种浏览器可以识别的方式显示；
*   客户端渲染：采用`ajax等异步操作请求数据`，速度更快；但不利于 SEO，爬虫抓不到异步数据（在源代码中看不到数据：如京东商品的评论区分页功能）；
*   服务端渲染：直接传过来带数据的 html 页面，爬虫在源代码中能找到数据，有利于 SEO；（在网页源代码中可以看到数据，如京东商品展示功能）
*   所以一般网站前后端渲染都会用到，为了更快、也为了 SEO。

**十三、服务器对静态资源的处理**

> **背景**：  
> 当我们在 html 页面中使用`link、script、img、iframe、video、audio`等需要再次发请求引入静态资源的标签时，其实就是自动又向服务器发了一次请求（请求路径分为：网络路径、url 文件路径会拼接在服务器地址后面；），所以服务器端也会对这些请求做响应。（如果没有响应，浏览器就会一直处于等待状态，没法渲染页面）

> **处理方式**：  
> 服务器将静态资源统一放到一个文件夹`public`中，然后在 html 页面中通过文件路径引用，这样可以通过`req.url`判断只要是以`/public/`开头的就直接把这个`url`当做文件路径去找这个文件，然后响应回去；所以 html 页面中使用的路径要是文件路径。

**十四、服务器对表单提交的处理**

*   传统`req.url`返回的是整个根目录及以后的部分；包含了路径和`query`信息；
*   当客户端使用`get`请求时，服务器要想得到`query`数据，单从`req.url`中不容易获取，所以有了专门处理路径的核心模块：`var url = require('url')`；
*   使用这个模块的`parse`方法可以得到一个路径对象；
*   `var pathObj = url.parse(req.url,true)`；第二个参数用于将`query`的属性值以对象形式呈现，默认是字符串，这里会涉及编码格式；
*   然后就是判断`pathObj.pathname`路径字符串来决定响应内容；
*   并向模板中使用上`pathObj.query`对象；
*   比如，添加到已有数组中，并使用重定向让页面刷新；
    *   重定向：响应设置`302状态码`（临时重定向，再次发请求，浏览器不记住重定向后的地址，相当于每次都是第一次，还是会向原网址发请求），浏览器收到这个状态码，就直接去响应头中找`Location`；在响应头中设置`Location`告诉浏览器重定向的路径；
    *   `res.statusCode = 302 res.setHeader('Location','/') res.end()`
*   但是这一步不是数据持久化，服务器一重启新加的数据会没有。  
    ![](https://img-blog.csdnimg.cn/20200729181846475.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYW5nYW5r,size_16,color_FFFFFF,t_70#pic_center)

**十四、Node.js 的测试方法**

*   浏览器中有`F12`调试工具
*   node 中也有调试工具：`>node`命令行直接输命令，可以直接用 node 中 API，按`ctrl+c+c`退出。

**十五、Node.js 的模块系统**

> 模块分类：
> 
> *   核心模块
> *   第三方模块
> *   自定义模块

1、Node.js 中的模块化基于 Commen.JS；

*   导出的是：`module.exports`对象；内部默认`var module.exports={}; var exports = module.exports; return module.exports`
*   所以想导出什么，往对象中添加，一般导出单个用：`module.exports=`；导出多个用：`exports.属性名=`或`module.exports={}`

2、require 加载规则

*   优先从缓存加载；缓存有的就不执行内部代码，而是返回对象`module.exports`；
*   `require('fs')`：引入核心模块
*   `require('./aa.js')`：引入自定义模块 (路径方式)
*   `require('art-template')`：引入第三方模块  
    核心模块、第三方模块的加载：在`node_module`文件下的同名文件中找`package.json`中的`main`属性对应的值，如`index.js`，然后去这个文件并执行；如果`main`没有，那默认找`index.js`；本文件夹没有则往外找`package.json、index.js`，直到找到根目录。

3、`package.json`会自动记录同文件中 npm 下载时带`--save、--save-dev`的第三方模块；不带不记录；  
4、使用`npm init`会自动生成`package.json`文件；  
5、使用`npm install`会自动根据`package.json`中记录下载包；用于拷贝项目时下载包。  
6、[npm 命令](https://www.cnblogs.com/itlkNote/p/6830682.html)  
7、解决 npm 被墙问题（国外网站访问慢）：

*   使用`nrm`源管理器；可以用`npm`命令，但是源变了；
*   下载指定源：`npm install --global cnpm`；这是可以用新源：`cnpm init`；
*   `cnpm`是淘宝镜像，每 10 分钟从 npm 中更新一次包数据。
*   配置 npm 以指定源，`npm config list`查看：`npm config set registry https://registry.npm.taobao.org`；这样还是 npm 命令，源变了；

**十六、Node.js 的第三方模块 ：Express**

1、轻便的 web 服务器开发框架；（封装的`http`核心模块）  
2、安装`npm install express --save`  
3、访问路径：

*   公开指定目录：`app.use('/public/',express.static('./public/'))`；用户可以输入以`/public/`开头的路径；
*   指定单个目录（路由）：`app.get('/',function(req,res){})`；用户访问根目录时的情况；
*   默认：当用户输入没有定义的路径，`express`内部的设置方案时：返回`404`页面。

4、在 express 中的`res`响应方法会自动结束，不用`res.end()`

**十七、Node.js 的路径问题**

1、`fs`文件操作中文件路径的相对路径中`./`可以省略；  
2、`require`模块加载时的相对路径中`./`不能省，省略就是加载核心模块 / 第三方模块；  
3、相对路径含义：

*   `./aa.js`：当前目录中的`aa.js`
*   `/aa.js`：当前磁盘根目录中
*   `../aa.js`：上一级目录中

4、`c:/aa.js`：（绝对路径）c 盘根目录中

**十八、Node.js 的服务自动重启**

`nodemon`：用于修改代码保存后自动重启服务器；

*   `node install --global nodemom`  
    `nodemon aa.js`

**十九、express 的静态资源服务**

1、通过路由匹配访问指定资源：`app.get('/',function(req,res){})、app.post('/',function(req,res){})`  
2、通过公开指定目录访问目录内文件：

*   `app.use('/public/',express.static('./public/'))`：以`/public/`为根目录开头的路径，后面的部分会去相应文件中找，并以正确编码显示；
*   `app.use(express.static('./public/'))`：只要路由中没有定义的，会直接截取根目录`/`后面部分，去`./public/`文件夹内部中找，找到就显示；

3、使用模板引擎模块`art-template`

*   安装：`npm install --save art-template express-art-template`
*   配置：识别`.art`结尾的文件，并使用模板引擎；可以在`app.engine`中更改设置；
    *   var express = require(‘express’)
    *   var app = express()
    *   `app.engine('art',require('express-art-template'))`// 可改后缀名
    *   `app.set('views',path.join(__dirname,'./views/'))`// 更改默认的`views`查找目录
*   使用：内部设置自动去同目录下的`views`文件夹中查找这个模板文件（`res.render('index.art')`不传对象参数就是直接传页面信息）；
    *   `app.get('/',function(req,res) { res.render('index.art',{ user:{ name:'aaa' } }) })`// 自动结束响应
*   重定向方法：`res.redirect('/')`

4、获取请求数据

*   get 方法：`req.query`// 就是对象形式
*   post 方法：借助第三方模块`body-parser`，`res.body`也是对象形式；  
    ![](https://img-blog.csdnimg.cn/20200731213411875.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYW5nYW5r,size_16,color_FFFFFF,t_70#pic_center)

**二十、使用 express 实现增删改查数据（Create Update Read Delete ）**

1、CURD 起步

*   新建文件夹`npm init`，初始化`package.json`
*   安装第三方模块`express、art-template、express-art-template`
*   配置、使用模块，创建服务器文件；

2、以`.json`文件为数据存储方式，对文件数据进行 CURD

*   利用`fs`核心模块，读取文件数据；
*   将二进制数据`toString()`转为 json 字符串（或者`fs.readFile('./aa.json','utf8',function(err,data){})`）；
*   将 json 字符串`JSON.parse(data)`转为 json 对象；
*   最后使用内部属性`JSON.parse(data).students`，用来做模板引擎数据；

3、配置服务器端路由：`router.js`

*   使用 express 中的 router，`var router = express.Router()`–router.js
*   加载路由，`app.use(router)`–app.js

4、创建操作页面

*   添加学生页面
*   编辑学生页面
*   删除学生页面

5、封装对学生数据的操作：`students.js`

> 利用 ID 获取数据和保存编辑时注意：
> 
> *   通过`req.query、req.body`获取的提交数据是对象形式，但对象中属性值都是字符串类型（所以 id 属性也是），需要转变`student.id = parseInt(student.id)`；
> *   通过`JSON.parse(data)`将 json 文件中字符串转为对象形式时，内部属性值原本是什么类型还不变；
> 
> 删除前弹框确认：node 环境中没有 confirm，所以在模板页面中判断；
> 
> *   `<a href="/students/delete?id={{$value.id}}" onclick="if(confirm('确定删除?')==false)return false;">删除</a>`
> 
> 编辑页面男女性别选中的判断：

```
<script>
      window.onload = function () {
        if ("{{student.gender}}" == 0) {//express-art-template模块的语法
          document.getElementsByName('gender')[0].checked = 'checked';
        } else {
          document.getElementsByName('gender')[1].checked = 'checked';
        }
      }
    </script>
```

6、es6 方法

```
Array.prototype.find = function(Func){
	for(var i = 0;i<this.length;i++){
		if(Func(this[i],i)){
			return this[i]//i;返回‘i’，就是findIndex方法
		}
	}
}
```

*   find：

```
var id = '1'
    var stu = students.find(function(item,index){
      return item.id == parseInt(id)
    })
```

*   findIndex：

```
var id = 1
    var delId = students.findIndex(function(item,index){
      return item.id == parseInt(id)
    })
```

7、异步编程–回调函数

> 用于得到一个函数内部异步操作的结果，在异步函数内部调用执行；

*   常见异步操作：
    *   setTimeout、readFile、writeFile、ajax
*   使用方式：`正常函数`–>`传参数：`–>`正常函数中使用异步操作`–>`在异步操作中调用这个回调函数`–>`并将异步操作的值传给这个回调函数作参数`；

```
function add(x,y,callback){
	//var x = 10
	//var y = 20
	//var callback = function(sum){...}
	setTimout(function(){
		var sum = x+y
		callback(sum)
	},1000)
}
add(10,20,function(sum){
	return sum
})//30,函数内部执行function
```

**二十一、JavaScript 模块化及其他补充**

*   node.js 中模块化：借助 CommonJS
*   EcmaScript 6 中：自带的模块化规范（官方规范）
*   浏览器中模块化：借助第三方库
    *   require.js：也称为 AMD 规范
    *   sea.js：也称为 CMD 规范
*   EcmaScript 6：通过编译器工具打包–EcmaScript 5；以防止浏览器不支持；
*   新技术的目的是为了提高效率，增加可维护性，可以利用编译器工具打包让低版本浏览器可以运行。
*   npm5 版本以上，`npm init`时会自动生成`package.json`，当下载包时，会自动生成`package-lock.json`文件，记录下载包以其依赖包的信息（真正版本号、下载地址等），这样当拷贝项目时`npm install`时就会参考这个文件；
    *   作用：使包的下载速度更快且与开发时版本一样，没有这个锁文件就会安装最新版本的包。

**二十二、MongoDB 数据库**

> MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。  
> MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。

1、(NoSQL)MongoDB 是一个面向文档存储的数据库，操作起来比较简单和容易。  
2、下载、安装、配置环境变量：bin 文件目录（用于全局使用）  
![](https://img-blog.csdnimg.cn/2020081018163186.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYW5nYW5r,size_16,color_FFFFFF,t_70)

*   MongoDB compass：可视化工具，类似 mysql 等关系型数据库所使用的`navicat`数据库管理工具；
*   现在`Navicat`也支持 mongodb 数据库了：`Navicat for MongoDB`；

3、检查安装是否成功：`mongod --version`  
4、基本使用：

*   手动创建数据存储目录：在某盘根目录下创建：`D:\data\db`
    
*   修改数据库存储目录：`mongod --dbpath=数据库存储目录路径`//`mongod --dbpath=D:\Mongodb\4.0\data`；修改前关闭本地 MongoDB 服务；  
    ![](https://img-blog.csdnimg.cn/20200810193218867.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYW5nYW5r,size_16,color_FFFFFF,t_70#pic_center)
    
*   开启数据库服务命令：`> mongod`
    
*   关闭数据库：`ctrl+c`
    
*   连接数据库：`mongo`
    
*   关闭连接：`exit`
    
*   查看所有数据库：`show dbs`；默认由系统数据库
    
*   查看当前数据库：`db`；默认有个`test`数据库，只有添加数据后才能在查看所有数据库时看到；
    
*   切换至指定数据库，没有就创建：`use [数据库名称]`；也是添加数据后才能用`show dbs`看到；
    
*   创建一条数据：`db.stu.insertOne({"name":"Jack"})`
    
*   查看当前数据库中集合：`show collections`//stu，类似数组
    
*   查看集合中数据：`db.stu.find() //{"_id":ObjectId("[自动生成]"),"name":"Jack"}`  
    ![](https://img-blog.csdnimg.cn/20200810193250293.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYW5nYW5r,size_16,color_FFFFFF,t_70#pic_center)