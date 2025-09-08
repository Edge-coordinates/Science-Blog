---
title: node 里 exports 的用法
date: 2022/10/14
categories:
  - - Language
    - Javascript
    - Nodejs
tags: null
abbrlink: 7fa08968
---



> 本文转自[CSDN](https://blog.csdn.net/chijiajing/article/details/83147965)

- [共享变量](#共享变量)
- [共享方法](#共享方法)
- [共享构造](#共享构造)
- [共享类](#共享类)

exports 可以共享方法、变量、构造、类。  
exports 的本质是一个数组，访问域是共有的。

```js
//打印一下exports
console.log(exports);
//结果是一个空数组
```

共享变量
====

exportDemo.js(被引用的)

```js
//打印一下exports
console.log(exports);
//结果是一个空数组
 
//共享变量
var aa=123;
exports.aa=aa;
//打印的结果是一个键值对关系的数组{aa:123}
console.log(exports);
```

exportsUse.js(引用方)

```js
//导入被引用的js文件
var exportsDemo=require("./exportsDemo.js");
 
//直接调用aa,这里的aa对应的是exports对应的key
console.log(exportsDemo.aa);
```

共享方法
====

exportDemo.js(被引用的)

```js
//打印一下exports
console.log(exports);
//结果是一个空数组
 
//共享方法
function aa(num1,num2){
	console.log("被共享的方法哦~");
	return (num1+num2);
}
 
//注意共享方法不能有小括号(哪怕是有参方法),一但有了括号就会根据return的内容直接返回对应的值
exports.aa=aa;
console.log(exports);
//打印结果: {aa:[Function:aa]}
 
//若加了括号
exports.bb=aa();
console.log(exports);
//打印结果:{aa:[Function:aa],bb:NaN}
```

exportsUse.js(引用方)

```js
//导入被引用的js文件
var exportsDemo=require("./exportsDemo.js");
 
//直接调用aa,这里的aa对应的是exports对应的key
console.log(exportsDemo.aa(2,5));
//打印的结果是 被共享的方法哦~ 7
```

共享构造
====

exportDemo.js(被引用的)

```js
//定义一个构造方法
 function Person(name,age,sex){
 	this.name=name;
 	this.age=age;
 	this.sex=sex;
 }
//这里就需要用到module了,module使用场景：类、构造方法
module.exports=Person;
console.log(exports);
//打印结果为空
```

exportsUse.js(引用方)

```js
//导入被引用的js文件
var exportsDemo=require("./exportsDemo.js");
 
var per=new exportsDemo("吴师傅",18,"男");
console.log(per);
//打印结果Person { name: '吴师傅', age: 18, sex: '男' }
```

共享类
===

exportDemo.js(被引用的)

```js
var React=require("react");
var ReactDom=require("react-dom");
 
class Header extends React.Component{
	render(){
		return (<div>这是头部</div>)
	}
}
 
module.exports=Header;
```


exportsUse.js(引用方)

```js
var React=require("react");
var ReactDom=require("react-dom");
//导入子组件
var Header=require("./Header.jsx");
var Footer=require("./footer.jsx");
 
//例子：定义参数以及方法调用
class Main extends React.Component{
	//定义参数得放在constructor里
    constructor(){
    	//定义参数
    	super();
    	this.state={timer:0}
    }
    //自定方法每次加1
    tick(){
    	console.log(this);
    	this.setState({
    		timer:(this.state.timer+1)
    	})
    }
    //点击方法
    trach(){
        console.log("运行点击方法了")
    }
    //类似Vue里的created钩子函数
    componentDidMount(){
    	//若不用箭头函数包裹起方法(this.tick())那么tick里面的this就是一个window对象.会报错
    	//包裹起来后的this就是main,这样的this才能指向timer
    	setInterval(()=>{this.tick()},1000)
    }
	render(){
		return (
			<div>
			<Header/>
			<p>{this.state.timer}
            <span><button onClick={this.trach.bind(this)}>点击事件</button></span>
            </p>
			</div>
			)
	}
}
ReactDom.render(<Main/>,document.getElementById("box"));
```