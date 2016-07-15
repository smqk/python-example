#coding=utf-8
'''
变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间。
基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。

Python有五个标准的数据类型：
    Numbers（数字）：
        1，int（有符号整型）
        2，long（长整型[也可以代表八进制和十六进制]）
        3，float（浮点型）
        4，complex（复数）
    String（字符串）
    List（列表）
    Tuple（元组）
    Dictionary（字典）
'''


'''
Python数字
    长整型也可以使用小写"L"，但是还是建议您使用大写"L"，避免与数字"1"混淆。Python使用"L"来显示长整型。
Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
'''
#int（有符号整型）
i1 = 10     # 10进制
i2 = 060    # 8进制
i3 = -0x260 # 16进制
#long（长整型[也可以代表八进制和十六进制]）
l1 = 51924361L
l2 = 0122L
l3 = -0x19323L
#float（浮点型）
f1 = 15.20
f2 = 32.3e18
#complex（复数）
c1 = 3.14j
c2 = 9.322e-36j
c3 = 3e+26J



#Python字符串
str = 'Hello World!'
print str       # 输出完整字符串
print str[0]    # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[2:]   # 输出从第三个字符开始的字符串
print str * 2   # 输出字符串两次
print str + "TEST" # 输出连接的字符串

'''
Python列表
    列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（所谓嵌套）。
    列表用[ ]标识。是python最通用的复合数据类型。看这段代码就明白。
    列表中的值得分割也可以用到变量[头下标:尾下标]，就可以截取相应的列表，从左到右索引默认0开始的，从右到左索引默认-1开始，下标可以为空表示取到头或尾。
    加号（+）是列表连接运算符，星号（*）是重复操作。如下实例：
'''
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list      # 输出完整列表
print list[0]   # 输出列表的第一个元素
print list[1:3] # 输出第二个至第三个的元素 
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2      # 输出列表两次
print list + tinylist   # 打印组合的列表


'''
Python元组
    元组是另一个数据类型，类似于List（列表）。
    元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
'''
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple         # 输出完整元组
print tuple[0]      # 输出元组的第一个元素
print tuple[1:3]    # 输出第二个至第三个的元素 
print tuple[2:]     # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2 # 输出元组两次
print tuple + tinytuple # 打印组合的元组


'''
Python元字典
    字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
    两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
    字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one']   # 输出键为'one' 的值
print dict[2]       # 输出键为 2 的值
print tinydict      # 输出完整的字典
print tinydict.keys()   # 输出所有键
print tinydict.values() # 输出所有值



