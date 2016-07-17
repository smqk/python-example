#coding=utf-8
'''
模块让你能够有逻辑地组织你的Python代码段。
把相关的代码分配到一个 模块里能让你的代码更好用，更易懂。
模块也是Python对象，具有随机的名字属性用来绑定或引用。
简单地说，模块就是一个保存了Python代码的文件。模块能定义函数，类和变量。模块里也能包含可执行的代码。
'''

#导入模块
import customerModule
#调用模块里面的函数
customerModule.print_fun("Python ")


'''
From…import 语句
    Python的from语句让你从模块中导入一个指定的部分到当前命名空间中。
语法如下：
    from modname import name1[, name2[, ... nameN]]
例如，要导入模块fib的fibonacci函数，使用如下语句：
    from fib import fibonacci
这个声明不会把整个fib模块导入到当前的命名空间中，它只会将fib里的fibonacci单个引入到执行这个声明的模块的全局符号表。
'''


'''
From…import* 语句
把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明： 
    from modname import *
    这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。 
'''


'''
 定位模块

当你导入一个模块，Python解析器对模块位置的搜索顺序是：
    当前目录
    如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
    如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。

模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。
'''


'''
dir()函数
    dir()函数——返回一个模块里定义的所有模块、变量、函数的名称排好序的字符串列表

如下一个简单的实例：
'''
import math
content = dir(math)
print(content);


'''
globals()和locals()函数

globals()和locals()函数可被用来返回全局和局部命名空间里的名字。
如果在函数内部调用locals()，返回的是所有能在该函数里访问的命名。
如果在函数内部调用globals()，返回的是所有在该函数里能访问的全局名字。
两个函数的返回类型都是字典。所以名字们能用keys()函数摘取。
'''


'''
reload()函数

当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
因此，如果你想重新执行模块里顶层部分的代码，可以用reload()函数。该函数会重新导入之前导入过的模块。语法如下：
    reload(module_name)
在这里，module_name要直接放模块的名字，而不是一个字符串形式。比如想重载hello模块，如下：
    reload(hello)
'''