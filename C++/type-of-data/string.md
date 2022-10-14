---
title: string
categories:
  - C++
tags:
  - type-of-data
abbrlink: 9ebeb2a9
---


> 原文链接 http://citycowboy.blog.sohu.com/50058804.html
> 做了一定整理和改动

**前言**

之所以抛弃 char\*的字符串而选用 C++标准程序库中的 string 类，是因为他和前者比较起来，不必担心内存是否足够、字符串长度等等，而且作为一个泛型类出现，他集成的操作函数足以完成我们大多数情况下(甚至是 100%)的需要。我们可以用 = 进行赋值操作，== 进行比较，+ 做串联（是不是很简单?）。我们可以把它看成是 C++的基本数据类型。
C++中对于 strinig 的定义为：typedef basic_string string; 也就是说 C++中的 string 类是一个泛型类，由模板而实例化的一个标准类，本质上不是一个标准数据类型。

# 正文
[toc]
好了，进入正题………
首先，为了在我们的程序中使用 string 类型，我们必须包含头文件 。如下：

```cpp
#include<string> //注意这里不是 string.h string.h 是 C 字符串头文件
using namespace std; //此语句必不可少，否则有的编译器无法识别
```

## 1．声明一个 C++字符串
声明一个字符串变量很简单：
```cpp
string str;
```
这样我们就声明了一个字符串变量，但既然是一个类，就有构造函数和析构函数。上面的声明没有传入参数，所以就直接使用了 string 的默认的构造函数，这个函数所作的就是把 Str 初始化为一个空字符串。
### String 类的构造函数和析构函数：
a) string s; //生成一个空字符串 s
b) string s(str) //拷贝构造函数 生成 str 的复制品
c) string s(str,stridx) //将字符串 str 内“始于位置 stridx”的部分当作字符串的初值
d) string s(str,stridx,strlen) //将字符串 str 内“始于 stridx 且长度顶多 strlen”的部分作为字符串的初值
e) string s(cstr) //将 C 字符串作为 s 的初值
f) string s(chars,chars_len) //将 C 字符串前 chars_len 个字符作为字符串 s 的初值。
g) string s(num,c) //生成一个字符串，包含 num 个 c 字符
h) string s(beg,end) //以区间 beg;end(不包含 end)内的字符作为字符串 s 的初值
i) s.~string() //销毁所有字符，释放内存
都很简单，我就不解释了。

## 2．字符串操作函数
这里是 C++字符串的重点，我先把各种操作函数罗列出来，不喜欢把所有函数都看完的人可以在这里找自己喜欢的函数，再到后面看他的详细解释。
a) =,assign() //赋以新值
b) swap() //交换两个字符串的内容
c) +=,append(),push_back() //在尾部添加字符
d) insert() //插入字符
e) erase() //删除字符
f) clear() //删除全部字符
g) replace() //替换字符
h) + //串联字符串
i) ==,!=,<,<=,>,>=,compare() //比较字符串
j) size(),length() //返回字符数量
k) max_size() //返回字符的可能最大个数
l) empty() //判断字符串是否为空
m) capacity() //返回重新分配之前的字符容量
n) reserve() //保留一定量内存以容纳一定数量的字符
o) [ ], at() //存取单一字符
p) >>,getline() //从 stream 读取某值
q) << //将谋值写入 stream
r) copy() //将某值赋值为一个 C_string
s) c_str() //将内容以 C_string 返回
t) data() //将内容以字符数组形式返回
u) substr() //返回某个子字符串
v)查找函数
w)begin() end() //提供类似 STL 的迭代器支持
x) rbegin() rend() //逆向迭代器
y) get_allocator() //返回配置器

**下面详细介绍：**
2．1 C++字符串和 C 字符串的转换
C++提供的由 C++字符串得到对应的 C_string 的方法是使用 data()、c_str()和 copy()，其中，data()以字符数组的形式返回字符串内容，但并不添加’\0’。c_str()返回一个以‘\0’结尾的字符数组，而 copy()则把字符串的内容复制或写入既有的 c_string 或字符数组内。C++字符串并不以’\0’结尾。我的建议是在程序中能使用 C++字符串就使用，除非万不得已不选用 c_string。由于只是简单介绍，详细介绍掠过，谁想进一步了解使用中的注意事项可以给我留言(到我的收件箱)。我详细解释。
2．2 大小和容量函数
一个 C++字符串存在三种大小：a)现有的字符数，函数是 size()和 length()，他们等效。Empty()用来检查字符串是否为空。b)max_size() 这个大小是指当前 C++字符串最多能包含的字符数，很可能和机器本身的限制或者字符串所在位置连续内存的大小有关系。我们一般情况下不用关心他，应该大小足够我们用的。但是不够用的话，会抛出 length_error 异常 c)capacity()重新分配内存之前 string 所能包含的最大字符数。这里另一个需要指出的是 reserve()函数，这个函数为 string 重新分配内存。重新分配的大小由其参数决定，默认参数为 0，这时候会对 string 进行非强制性缩减。

还有必要再重复一下 C++字符串和 C 字符串转换的问题，许多人会遇到这样的问题，自己做的程序要调用别人的函数、类什么的（比如数据库连接函数 Connect(char*,char*)），但别人的函数参数用的是 char*形式的，而我们知道，c_str()、data()返回的字符数组由该字符串拥有，所以是一种 const char*,要想作为上面提及的函数的参数，还必须拷贝到一个 char*,而我们的原则是能不使用 C 字符串就不使用。那么，这时候我们的处理方式是：如果此函数对参数(也就是 char*)的内容不修改的话，我们可以这样 Connect((char*)UserID.c_str(), (char*)PassWD.c_str()),但是这时候是存在危险的，因为这样转换后的字符串其实是可以修改的（有兴趣地可以自己试一试），所以我强调除非函数调用的时候不对参数进行修改，否则必须拷贝到一个 char*上去。当然，更稳妥的办法是无论什么情况都拷贝到一个 char*上去。同时我们也祈祷现在仍然使用 C 字符串进行编程的高手们（说他们是高手一点儿也不为过，也许在我们还穿开裆裤的时候他们就开始编程了，哈哈…）写的函数都比较规范，那样我们就不必进行强制转换了。

2．3 元素存取
我们可以使用下标操作符[]和函数 at()对元素包含的字符进行访问。但是应该注意的是操作符[]并不检查索引是否有效（有效索引 0~str.length()），如果索引失效，会引起未定义的行为。而 at()会检查，如果使用 at()的时候索引无效，会抛出 out_of_range 异常。
有一个例外不得不说，const string a;的操作符[]对索引值是 a.length()仍然有效，其返回值是’\0’。其他的各种情况，a.length()索引都是无效的。举例如下：
const string Cstr(“const string”);
string Str(“string”);

Str[3]; //ok
Str.at(3); //ok

Str[100]; //未定义的行为
Str.at(100); //throw out_of_range

Str[Str.length()] //未定义行为
Cstr[Cstr.length()] //返回 ‘\0’
Str.at(Str.length());//throw out_of_range
Cstr.at(Cstr.length()) ////throw out_of_range

我不赞成类似于下面的引用或指针赋值：
char& r=s[2];
char\* p= &s[3];
因为一旦发生重新分配，r,p 立即失效。避免的方法就是不使用。

2．4 比较函数
C++字符串支持常见的比较操作符（>,>=,<,<=,==,!=），甚至支持 string 与 C-string 的比较(如 str<”hello”)。在使用>,>=,<,<=这些操作符的时候是根据“当前字符特性”将字符按字典顺序进行逐一得比较。字典排序靠前的字符小，比较的顺序是从前向后比较，遇到不相等的字符就按这个位置上的两个字符的比较结果确定两个字符串的大小。同时，string(“aaaa”)
另一个功能强大的比较函数是成员函数 compare()。他支持多参数处理，支持用索引值和长度定位子串来进行比较。他返回一个整数来表示比较结果，返回值意义如下：0-相等〉0-大于 <0-小于。举例如下：
string s(“abcd”);

    s.compare(“abcd”); //返回0
    s.compare(“dcba”); //返回一个小于0的值
    s.compare(“ab”); //返回大于0的值

s.compare(s); //相等
s.compare(0,2,s,2,2); //用”ab”和”cd”进行比较 小于零
s.compare(1,2,”bcx”,2); //用”bc”和”bc”比较。
怎么样？功能够全的吧！什么？还不能满足你的胃口？好吧，那等着，后面有更个性化的比较算法。先给个提示，使用的是 STL 的比较算法。什么？对 STL 一窍不通？靠，你重修吧！

2．5 更改内容
这在字符串的操作中占了很大一部分。
首先讲赋值，第一个赋值方法当然是使用操作符=，新值可以是 string(如：s=ns) 、c_string(如：s=”gaint”)甚至单一字符（如：s=’j’）。还可以使用成员函数 assign()，这个成员函数可以使你更灵活的对字符串赋值。还是举例说明吧：
s.assign(str); //不说
s.assign(str,1,3);//如果 str 是”iamangel” 就是把”ama”赋给字符串
s.assign(str,2,string::npos);//把字符串 str 从索引值 2 开始到结尾赋给 s
s.assign(“gaint”); //不说
s.assign(“nico”,5);//把’n’ ‘I’ ‘c’ ‘o’ ‘\0’赋给字符串
s.assign(5,’x’);//把五个 x 赋给字符串
把字符串清空的方法有三个：s=””;s.clear();s.erase();(我越来越觉得举例比说话让别人容易懂！)。
string 提供了很多函数用于插入（insert）、删除（erase）、替换（replace）、增加字符。
先说增加字符（这里说的增加是在尾巴上），函数有 +=、append()、push_back()。举例如下：
s+=str;//加个字符串
s+=”my name is jiayp”;//加个 C 字符串
s+=’a’;//加个字符

s.append(str);
s.append(str,1,3);//不解释了 同前面的函数参数 assign 的解释
s.append(str,2,string::npos)//不解释了

s.append(“my name is jiayp”);
s.append(“nico”,5);
s.append(5,’x’);

s.push_back(‘a’);//这个函数只能增加单个字符 对 STL 熟悉的理解起来很简单

也许你需要在 string 中间的某个位置插入字符串，这时候你可以用 insert()函数，这个函数需要你指定一个安插位置的索引，被插入的字符串将放在这个索引的后面。
s.insert(0,”my name”);
s.insert(1,str);
这种形式的 insert()函数不支持传入单个字符，这时的单个字符必须写成字符串形式(让人恶心)。既然你觉得恶心，那就不得不继续读下面一段话：为了插入单个字符，insert()函数提供了两个对插入单个字符操作的重载函数：insert(size_type index,size_type num,chart c)和 insert(iterator pos,size_type num,chart c)。其中 size_type 是无符号整数，iterator 是 char\*,所以，你这么调用 insert 函数是不行的：insert(0,1,’j’);这时候第一个参数将转换成哪一个呢？所以你必须这么写：insert((string::size_type)0,1,’j’)！第二种形式指出了使用迭代器安插字符的形式，在后面会提及。顺便提一下，string 有很多操作是使用 STL 的迭代器的，他也尽量做得和 STL 靠近。
删除函数 erase()的形式也有好几种（真烦！），替换函数 replace()也有好几个。举例吧：
string s=”il8n”;
s.replace(1,2,”nternationalizatio”);//从索引 1 开始的 2 个替换成后面的 C_string
s.erase(13);//从索引 13 开始往后全删除
s.erase(7,5);//从索引 7 开始往后删 5 个

2．6 提取子串和字符串连接

题取子串的函数是：substr(),形式如下：
s.substr();//返回 s 的全部内容
s.substr(11);//从索引 11 往后的子串
s.substr(5,6);//从索引 5 开始 6 个字符
把两个字符串结合起来的函数是+。（谁不明白请致电 120）

2．7 输入输出操作
1．>> 从输入流读取一个 string。
2．<< 把一个 string 写入输出流。
另一个函数就是 getline(),他从输入流读取一行内容，直到遇到分行符或到了文件尾。

2．8 搜索与查找
查找函数很多，功能也很强大，包括了：
find()
rfind()
find_first_of()
find_last_of()
find_first_not_of()
find_last_not_of()
这些函数返回符合搜索条件的字符区间内的第一个字符的索引，没找到目标就返回 npos。所有的函数的参数说明如下：
第一个参数是被搜寻的对象。第二个参数（可有可无）指出 string 内的搜寻起点索引，第三个参数（可有可无）指出搜寻的字符个数。比较简单，不多说不理解的可以向我提出，我再仔细的解答。当然，更加强大的 STL 搜寻在后面会有提及。
最后再说说 npos 的含义，string::npos 的类型是 string::size_type,所以，一旦需要把一个索引与 npos 相比，这个索引值必须是 string::size)type 类型的，更多的情况下，我们可以直接把函数和 npos 进行比较（如：if(s.find(“jia”)==string::npos)）。
第二部分是关于 C++字符串对迭代器的支持的，视大家的需要我将写出来（意思就是不需要就算了，我乐得轻省，哈哈…）。
好了，大概的对 string 类型进行了阐述，希望起到抛砖引玉的作用，让初学者对 string 有个了解而不必已开始就面对复杂的内部结构和无数个注意事项。对字符串更详细地讲解有很多参考书，其实我的内容也是从 C++标准程序库得来的，加上几句自己的看法，所以要感谢这本书的作者和译者。任何人对本文进行引用都要标明作者是 Nicolai M.Josuttis 译者是侯捷/孟岩。不过不要提及我，任何观点的错误都与我无关（除了这里边体现我主观想法的几句话，也就那几句话）。

### string 函数列表

```
函数名 描述
begin 得到指向字符串开头的 Iterator
end 得到指向字符串结尾的 Iterator
rbegin 得到指向反向字符串开头的 Iterator
rend 得到指向反向字符串结尾的 Iterator
size 得到字符串的大小
length 和 size 函数功能相同
max_size 字符串可能的最大大小
capacity 在不重新分配内存的情况下，字符串可能的大小
empty 判断是否为空
operator[] 取第几个元素，相当于数组
c_str 取得 C 风格的 const char\* 字符串
data 取得字符串内容地址
operator= 赋值操作符
reserve 预留空间
swap 交换函数
insert 插入字符
append 追加字符
push_back 追加字符
operator+= += 操作符
erase 删除字符串
clear 清空字符容器中所有内容
resize 重新分配空间
assign 和赋值操作符一样
replace 替代
copy 字符串到空间
find 查找
rfind 反向查找
find_first_of 查找包含子串中的任何字符，返回第一个位置
find_first_not_of 查找不包含子串中的任何字符，返回第一个位置
find_last_of 查找包含子串中的任何字符，返回最后一个位置
find_last_not_of 查找不包含子串中的任何字符，返回最后一个位置
substr 得到字串
compare 比较字符串
operator+ 字符串链接
operator== 判断是否相等
operator!= 判断是否不等于
operator<</td> 判断是否小于
operator>> 从输入流中读入字符串
operator<< 字符串写入输出流
getline 从输入流中读入一行
```

string 是非常强大的类型，很好的封装了字符串的操作，有些时候我们可以把 string 当做字符的容器，string 也支持大多数容器操作，下面就列出 string 类型所支持的所有操作，本文并不是为了讲解 string 的用法和应用，而是希望作为 string 类型的参考文档，每个函数皆在注释后有详细说明，需要用时查阅即可。

1.构造函数
```cpp
string();//空串

string(size_type length,char ch);//以 length 为长度的 ch 的拷贝（即 length 个 ch）

string(const char \*str);//以 str 为初值 (长度任意)

string(const char \*str,size_type length);//同上，长度不限，但注意不要越界，以免发生不可预知问题

string(string &str, size_type index, size_type length);  
//以 index 为索引开始的子串，长度为 length, 或者小于 length

string(input_iterator begin, input_iterator end);//以从 start 到 end 的元素为初值  
2.支持的操作符
== >
< >=
<=
!= +
+=
[ ] 3.追加文本（append）

[cpp] view plain copy
basic_string &append(const basic_string &str);//在字符串的末尾添加 str

basic_string &append(const char \*str);//在字符串末尾添加 str 所指向的 c 风格字符串

basic_string &append(const basic_string &str,size_type index,size_type len);  
//在字符串的末尾添加 str 的子串,子串以 index 索引开始，长度为 len

basic_string &append(const char \*str,size_type num);//在字符串的末尾添加 str 中的 num 个字符

basic_string &append(size_type num,char ch);//在字符串的末尾添加 num 个字符 ch

basic_string &append(input_iterator start,input_iterator end);  
//在字符串的末尾添加以迭代器 start 和 end 表示的字符序列

push_back('k');//把一个字符连接到当前字符串的结尾  
4.赋值（assign）

[cpp] view plain copy
basic_string &assign(const basic_string &str);//用 str 为字符串赋值

basic_string &assign(const char \*str);//用 str c 风格为字符串赋值

basic_string &assign(const char \*str,size_type num);//用 str 的开始 num 个字符为字符串赋值

basic_string &assign(const basic_string &str,size_type index,size_type len);  
//用 str 的子串为字符串赋值,子串以 index 索引开始，长度为 len

basic_string &assign(size_type num,char ch);//用 num 个字符 ch 为字符串赋值

string &assign(const_iterator begin,const_itertor end);  
//把 first 和 last 迭代器之间的部分赋给字符串  
5.比较（compare）

[cpp] view plain copy
int compare(const basic_string &str);//比较自己和 str

int compare(size_type index,size_type length,const basic_string &str);  
//比较自己的子串和 str,子串以 index 索引开始，长度为 length

int compare(size_type index,size_type length,const basic_string &str,size_type  
 index2,size_type length2);  
//比较自己的子串和 str 的子串，其中 index2 和 length2 引用 str，index 和 length 引用自己

int compare(const char \*str);//比较自己和 str

int compare(int pos, int n,const char \*s)  
//比较自己的子串，从 pos 开始，n 个字符，和 s 进行比较

int compare(size_type index,size_type length,const char \*str,size_type length2);  
//比较自己的子串和 str 的子串，其中 str 的子串以索引 0 开始，长度为 length2，自己的子串  
//以 index 开始，长度为 length  
 返回值 情况

      小于零        this < str
      零                this == str
      大于零        this > str

6.删除（erase）

[cpp] view plain copy
iterator erase(iterator first, iterator last);  
//删除[first，last）之间的所有字符，返回删除后迭代器的位置

iterator erase(iterator it);//删除 it 指向的字符，返回删除后迭代器的位置

string &erase(int pos = 0, int n = npos);//删除 pos 开始的 n 个字符，返回修改后的字符串  
7.插入（insert）

[cpp] view plain copy
iterator insert(iterator i,const char &ch);//在迭代器 i 表示的位置前面插入一个字符 ch

basic_string &insert(size_type index,const basic_string &str);//在字符串的位置 index 插入字符串 str

basic_string &insert(size_type index,const char \*str);//在字符串的位置 index 插入字符串 str

basic_string &insert(size_type index1,const basic_string &str,size_type index2,size_type num);  
//在字符串的位置 index 插入字符串 str 的子串(从 index2 开始，长 num 个字符)

basic_string &insert(size_type index,const char \*str,size_type num);  
//在字符串的位置 index 插入字符串 str 的 num 个字符

basic_string &insert(size_type index,size_type num,char ch );  
//在字符串的位置 index 插入 num 个字符 ch 的拷贝

void insert(iterator i,size_type num,const char &ch);  
//在迭代器 i 表示的位置前面插入 num 个字符 ch 的拷贝

void insert(iterator i,iterator begin,iterator end );  
//在迭代器 i 表示的位置前面插入一段字符，从 start 开始，以 end 结束  
8.替换（replace）

[cpp] view plain copy
basic_string &replace(size_type index,size_type num,const basic_string &str);  
//用 str 中的 num 个字符替换本字符串中的字符,从 index 开始

replace(size_type index1,size_type num1,const basic_string &str,size_type index2,size_type num2);  
//用 str 中的 num2 个字符（从 index2 开始）替换本字符串中的字符，从 index1 开始，最多 num1 个字符

basic_string &replace(size_type index,size_type num,const char \*str);  
//用 str 中的 num 个字符（从 index 开始）替换本字符串中的字符

basic_string &replace(size_type index,size_type num1,const char \*str,size_type num2);  
//用 str 中的 num2 个字符（从 index2 开始）替换本字符串中的字符，从 index1 开始，num1 个字符

basic_string &replace(size_type index,size_type num1,size_type num2,char ch);  
//用 num2 个 ch 字符替换本字符串中的字符，从 index 开始，num1 个字符

basic_string &replace(iterator start,iterator end,const basic_string &str);  
//用 str 中的字符替换本字符串中的字符,迭代器 start 和 end 指示范围

basic_string &replace(iterator start,iterator end,const char \*str);  
//用 str 替换本字符串中的内容,迭代器 start 和 end 指示范围

basic_string &replace(iterator start,iterator end,const char \*str,size_type num );  
//用 str 中的 num 个字符替换本字符串中的内容,迭代器 start 和 end 指示范围

basic_string &replace(iterator start,iterator end,size_type num,char ch );  
//用 num 个 ch 字符替换本字符串中的内容，迭代器 start 和 end 指示范围  
9.查找

[cpp] view plain copy
函数 find:

size_type find( const basic_string &str, size_type index );  
//返回 str 在字符串中第一次出现的位置（从 index 开始查找）

size_type find( const char \*str, size_type index );  
//返回 str 在字符串中第一次出现的位置（从 index 开始查找）

size_type find( const char \*str, size_type index, size_type length );  
//返回 str 在字符串中第一次出现的位置（从 index 开始查找，长度为 length）

size_type find( char ch, size_type index );  
//返回字符 ch 在字符串中第一次出现的位置（从 index 开始查找）

函数 find_first_of:查找在字符串中第一个与 str 中的某个字符匹配的字符

    size_type find_first_of( const basic_string &str, size_type index = 0);

    size_type find_first_of( const char *str, size_type index = 0 );

    size_type find_first_of( const char *str, size_type index, size_type num );

    size_type find_first_of( char ch, size_type index = 0 );

函数 find_first_not_of:在字符串中查找第一个与 str 中的字符都不匹配的字符

    size_type find_first_not_of( const basic_string &str, size_type index = 0 );

    size_type find_first_not_of( const char *str, size_type index = 0 );

    size_type find_first_not_of( const char *str, size_type index, size_type num );

    size_type find_first_not_of( char ch, size_type index = 0 );

函数 find_last_of:在字符串中查找最后一个与 str 中的某个字符匹配的字符

size_type find_last_of( const basic_string &str, size_type index = npos );

size_type find_last_of( const char \*str, size_type index = npos );

size_type find_last_of( const char \*str, size_type index, size_type num );

size_type find_last_of( char ch, size_type index = npos );

函数 find_last_not_of:在字符串中查找最后一个与 str 中的字符都不匹配的字符

    size_type find_last_not_of( const basic_string &str, size_type index = npos );

    size_type find_last_not_of( const char *str, size_type index = npos);

    size_type find_last_not_of( const char *str, size_type index, size_type num );

    size_type find_last_not_of( char ch, size_type index = npos );

rfind 函数

size_type rfind( const basic_string &str, size_type index );  
 //返回最后一个与 str 中的某个字符匹配的字符，从 index 开始查找

size_type rfind( const char \*str, size_type index );  
 //返回最后一个与 str 中的某个字符匹配的字符，从 index 开始查找

size_type rfind( const char \*str, size_type index, size_type num );  
 //返回最后一个与 str 中的某个字符匹配的字符，从 index 开始查找,最多查找 num 个字符

size_type rfind( char ch, size_type index );  
 //返回最后一个与 ch 匹配的字符，从 index 开始查找

10.其他函数

[cpp] view plain copy
at 函数  
 reference at( size_type index );  
 //at()函数返回一个引用，指向在 index 位置的字符. 如果 index  
 //不在字符串范围内, at() 将报告"out of range"错误，并抛出 out_of_range 异常

begin 函数  
 iterator begin();//begin()函数返回一个迭代器,指向字符串的第一个元素

end 函数  
 iterator end();//返回一个迭代器，指向字符串的末尾(最后一个字符的下一个位置)

c_str 函数  
 const char \*c_str();//返回一个指向正规 C 字符串的指针, 内容与本字符串相同

capacity 函数  
 size_type capacity();//返回在重新申请更多的空间前字符串可以  
 //容纳的字符数. 这个数字至少与 size()一样大

copy 函数  
 size_type copy( char \*str, size_type num, size_type index );  
 //拷贝自己的 num 个字符到 str 中（从索引 index 开始）。返回值是拷贝的字符数

data 函数  
 const char \*data();//返回指向自己的第一个字符的指针

empty 函数  
 bool empty();//如果字符串为空则 empty()返回真(true)，否则返回假(false)

get_allocator 函数  
 allocator_type get_allocator();//返回本字符串的配置器

length 函数  
 size_type length();//返回字符串的长度. 这个数字应该和 size()返回的数字相同

max_size  
 size_type max_size();//返回字符串能保存的最大字符数

rbegin 函数  
 rbegin();//返回一个逆向迭代器，指向最后一个字符

rend 函数  
 rend();//返回一个逆向迭代器，指向第一个元素的前一个位置

reserve 函数  
 reserve( size_type num );//保留一定容量以容纳字符串（设置 capacity 值）

resize 函数  
 void resize( size_type num );//改变本字符串的大小到 num, 新空间的内容不确定

void resize( size_type num, char ch );//也可以指定用 ch 填充

size 函数  
 size();//返回字符串中字符的数量

substr 函数  
 basic_string substr( size_type index, size_type num = npos );  
 //返回本字符串的一个子串，从 index 开始，长 num 个字符。如果没有指定，  
 //将是默认值 string::npos。这样，substr()函数将简单的返回从 index 开始的剩余的字符串

swap 函数  
 void swap( basic_string &str );//把 str 和本字符串交换

11.示例

[cpp] view plain copy
#include <iostream>  
#include <string>  
#include <sstream>  
using namespace std;  
int main(){  
 //1.string 类重载运算符 operator>>用于输入，同样重载运算符 operator<<用于输出操作  
 string str1;  
 cin >> str1;//当用 cin>>进行字符串的输入的时候，遇到空格的地方就停止字符串的读取输入  
 cout << str1 << endl;  
 cin.get();//这个的作用就是读取 cin>>输入的结束符，不用对 getline 的输入产生影响！  
 getline(cin, str1);//字符串的行输入  
 cout << str1 << endl;

    //2.string类的构造函数
    string str2 = "aaaaa";//最简单的字符串初始化
    cout << str2 << endl;

    char *s = "bbbbb";
    string str3(s);//用c字符串s初始化
    cout << str3 << endl;

    char ch = 'c';
    string str4(5, ch);//用n个字符ch初始化
    cout << str4 << endl;

    //3.string类的字符操作
    string str5 = "abcde";
    ch = str5[3];//operator[]返回当前字符串中第n个字符的位置
    cout << ch << endl;

    string str6 = "abcde";
    ch = str6.at(4);//at()返回当前字符串中第n个字符的位置,并且提供范围检查，当越界时会抛出异常！
    cout << ch << endl;

    //4.string的特性描述
    string str7 = "abcdefgh";
    int size;
    size = str7.capacity();//返回当前容量
    cout << size << endl;
    size = str7.max_size();//返回string对象中可存放的最大字符串的长度
    cout << size << endl;
    size = str7.size();//返回当前字符串的大小
    cout << size << endl;
    size = str7.length();//返回当前字符串的长度
    cout << size << endl;
    bool flag;
    flag = str7.empty();//判断当前字符串是否为空
    cout << flag << endl;
    int len = 10;
    str7.resize(len, ch);//把字符串当前大小置为len，并用字符ch填充不足的部分
    cout << str7 << endl;

    //5.string的赋值
    string str8;
    str8 = str7;//把字符串str7赋给当前字符串
    cout << str8 << endl;
    str8.assign(str7);//把字符串str7赋给当前字符串
    cout << str8 << endl;
    str8.assign(s);//用c类型字符串s赋值
    cout << str8 << endl;
    str8.assign(s, 2);//用c类型字符串s开始的n个字符赋值
    cout << str8 << endl;
    str8.assign(len, ch);//用len个字符ch赋值给当前字符串
    cout << str8 << endl;
    str8.assign(str7, 0, 3);//把字符串str7中从0开始的3个字符赋给当前字符串
    cout << str8 << endl;
    string str9 = "0123456789";
    str8.assign(str9.begin(), str9.end());//把迭代器之间的字符赋给字符串
    cout << str8 << endl;

    //6.string的连接
    string str10;
    str10 += str9;//把字符串str9连接到当前字符串的结尾
    cout << str10 << endl;
    str10.append(s);//把c类型字符串s连接到当前字符串的结尾
    cout << str10 << endl;
    str10.append(s, 2);//把c类型字符串s的前2个字符连接到当前字符串的结尾
    cout << str10 << endl;
    str10.append(str9.begin(), str9.end());//把迭代器之间的一段字符连接到当前字符串的结尾
    cout << str10 << endl;
    str10.push_back('k');//把一个字符连接到当前字符串的结尾
    cout << str10 << endl;

    //7.string的比较
    flag = (str9 == str10);//判断两个字符串是否相等
    cout << flag << endl;
    flag = (str9 != str10);//判断两个字符串是否不相等
    cout << flag << endl;
    flag = (str9 > str10);//判断两个字符串是否大于关系
    cout << flag << endl;
    flag = (str9 < str10);//判断两个字符串是否为小于关系
    cout << flag << endl;
    flag = (str9 >= str10);//判断两个字符串是否为大于等于关系
    cout << flag << endl;
    flag = (str9 <= str10);//判断两个字符串否为小于等于关系
    cout << flag << endl;

    //以下的3个函数同样适用于c类型的字符串，在compare函数中>时返回1，<时返回-1，=时返回0
    flag = str10.compare(str9);//比较两个字符串的大小，通过ASCII的相减得出！
    cout << flag << endl;
    flag = str10.compare(6, 12, str9);//比较str10字符串从6开始的12个字符组成的字符串与str9的大小
    cout << flag << endl;
    flag = str10.compare(6, 12, str9, 3, 5);//比较str10字符串从6开始的12个字符组成的字符串与str9字符串从3开始的5个字符组成的字符串的大小
    cout << flag << endl;

    //8.string的字串
    string str11;
    str11 = str10.substr(10, 15);//返回从下标10开始的15个字符组成的字符串
    cout << str11 << endl;

    //9.string的交换
    str11.swap(str10);//交换str11与str10的值
    cout << str11 << endl;

    //10.string的查找，查找成功时返回所在位置，失败时返回string::npos的值，即是-1
    string str12 = "abcdefghijklmnopqrstuvwxyz";
    int pos;
    pos = str12.find('i', 0);//从位置0开始查找字符i在当前字符串的位置
    cout << pos << endl;
    pos = str12.find("ghijk", 0);//从位置0开始查找字符串“ghijk”在当前字符串的位置
    cout << pos << endl;
    pos = str12.find("opqrstuvw", 0, 4);//从位置0开始查找字符串“opqrstuvw”前4个字符组成的字符串在当前字符串中的位置
    cout << pos << endl;
    pos = str12.rfind('s', string::npos);//从字符串str12反向开始查找字符s在字符串中的位置
    cout << pos << endl;
    pos = str12.rfind("klmn", string::npos);//从字符串str12反向开始查找字符串“klmn”在字符串中的位置
    cout << pos << endl;
    pos = str12.rfind("opqrstuvw", string::npos, 3);//从string::pos开始从后向前查找字符串s中前n个字符组成的字符串在当前串中的位置
    cout << pos << endl;

    string str13 = "aaaabbbbccccdddeeefffggghhhiiijjjkkllmmmandjfaklsdfpopdtwptioczx";
    pos = str13.find_first_of('d', 0);//从位置0开始查找字符d在当前字符串第一次出现的位置
    cout << pos << endl;
    pos = str13.find_first_of("eefff", 0);//从位置0开始查找字符串“eeefff“在当前字符串中第一次出现的位置
    cout << pos << endl;
    pos = str13.find_first_of("efff", 0, 3);//从位置0开始查找当前串中第一个在字符串”efff“的前3个字符组成的数组里的字符的位置
    cout << pos << endl;
    pos = str13.find_first_not_of('b', 0);//从当前串中查找第一个不在串s中的字符出现的位置
    cout << pos << endl;
    pos = str13.find_first_not_of("abcdefghij", 0);//从当前串中查找第一个不在串s中的字符出现的位置
    cout << pos << endl;
    pos = str13.find_first_not_of("abcdefghij", 0, 3);//从当前串中查找第一个不在由字符串”abcdefghij”的前3个字符所组成的字符串中的字符出现的位置
    cout << pos << endl;
    //下面的last的格式和first的一致，只是它从后面检索！
    pos = str13.find_last_of('b', string::npos);
    cout << pos << endl;
    pos = str13.find_last_of("abcdef", string::npos);
    cout << pos << endl;
    pos = str13.find_last_of("abcdef", string::npos, 2);
    cout << pos << endl;
    pos = str13.find_last_not_of('a', string::npos);
    cout << pos << endl;
    pos = str13.find_last_not_of("abcdef", string::npos);
    cout << pos << endl;
    pos = str13.find_last_not_of("abcdef", string::npos, 3);
    cout << pos << endl;

    //11.string的替换
    string str14 = "abcdefghijklmn";
    str14.replace(0, 3, "qqqq");//删除从0开始的3个字符，然后在0处插入字符串“qqqq”
    cout << str14 << endl;
    str14.replace(0, 3, "vvvv", 2);//删除从0开始的3个字符，然后在0处插入字符串“vvvv”的前2个字符
    cout << str14 << endl;
    str14.replace(0, 3, "opqrstuvw", 2, 4);//删除从0开始的3个字符，然后在0处插入字符串“opqrstuvw”从位置2开始的4个字符
    cout << str14 << endl;
    str14.replace(0, 3, 8, 'c');//删除从0开始的3个字符，然后在0处插入8个字符 c
    cout << str14 << endl;
    //上面的位置可以换为迭代器的位置，操作是一样的，在这里就不再重复了！

    //12.string的插入，下面的位置处亦可以用迭代器的指针表示，操作是一样的
    string str15 = "abcdefg";
    str15.insert(0, "mnop");//在字符串的0位置开始处，插入字符串“mnop”
    cout << str15 << endl;
    str15.insert(0, 2, 'm');//在字符串的0位置开始处，插入2个字符m
    cout << str15 << endl;
    str15.insert(0, "uvwxy", 3);//在字符串的0位置开始处，插入字符串“uvwxy”中的前3个字符
    cout << str15 << endl;
    str15.insert(0, "uvwxy", 1, 2);//在字符串的0位置开始处，插入从字符串“uvwxy”的1位置开始的2个字符
    cout << str15 << endl;

    //13.string的删除
    string str16 = "gfedcba";
    string::iterator it;
    it = str16.begin();
    it++;
    str16.erase(it);//删除it指向的字符，返回删除后迭代器的位置
    cout << str16 << endl;
    str16.erase(it, it+3);//删除it和it+3之间的所有字符，返回删除后迭代器的位置
    cout << str16 << endl;
    str16.erase(2);//删除从字符串位置3以后的所有字符，返回位置3前面的字符
    cout << str16 << endl;

    //14.字符串的流处理
    string str17("hello,this is a test");
    istringstream is(str17);
    string s1,s2,s3,s4;
    is>>s1>>s2>>s3>>s4;//s1="hello,this",s2="is",s3="a",s4="test"
    ostringstream os;
    os<<s1<<s2<<s3<<s4;
    cout<<os.str() << endl;

    //system("pause");

}
```