简介
==

毫无疑问，使用 python 运行命令行是最方便的将模型测试自动化的途径，下面详细介绍几种方案并作对比。

方案一：os.system
=============

仅仅在一个子终端运行系统命令，而不能获取命令执行后的返回信息

如果在命令行下执行，结果直接打印出来。

```
os.system('ls')
# 04101419778.CHM   bash      document    media      py-django   video
# 11.wmv            books     downloads   Pictures  python
# all-20061022      Desktop   Examples    project    tools
```

复制

方案二：os.popen
============

该方法不但执行命令还返回执行后的信息对象

```
import os
tmp = os.popen('ls *.py').readlines()
# ['dump_db_pickle.py ',
# 'dump_db_pickle_recs.py ',
# 'dump_db_shelve.py ',
# 'initdata.py ',
# '__init__.py ',
# 'make_db_pickle.py ',
# 'make_db_pickle_recs.py ',
# 'make_db_shelve.py ',
# 'peopleinteract_query.py ',
# 'reader.py ',
# 'testargv.py ',
# 'teststreams.py ',
# 'update_db_pickle.py ',
# 'writer.py ']
```

复制

好处在于：将返回的结果赋给一变量，便于程序处理。

方案三：使用模块 subprocess
===================

```
import subprocess
subprocess.call (["cmd", "arg1", "arg2"],shell=True)
```

复制

获取返回和输出:

```
import subprocess
p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line,
retval = p.wait()
```

复制

方案四： commands
=============

```
import commands
dir(commands)
# ['__all__', '__builtins__', '__doc__', '__file__', '__name__', 'getoutput', 'getstatus','getstatusoutput', 'mk2arg', 'mkarg']
commands.getoutput("date")
# 'Wed Jun 10 19:39:57 CST 2009'
commands.getstatusoutput("date")
# (0, 'Wed Jun 10 19:40:41 CST 2009')
```

复制

注意： 当执行命令的参数或者返回中包含了中文文字，那么建议使用 subprocess，如果使用 os.popen 则会出现下面的错误:

```
Traceback (most recent call last):
  File "./test1.py", line 56, in <module>
    main()
  File "./test1.py", line 45, in main
    fax.sendFax()
  File "./mailfax/Fax.py", line 13, in sendFax
    os.popen(cmd)
UnicodeEncodeError: 'ascii' codec can't encode characters in position 46-52: ordinal not inrange(128)
```
