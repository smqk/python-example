#coding=utf-8
if  True:
    print "True"
else:
    print "False"


# 井号为当行注释
# 使用斜杠（ \）将一行的语句分为多行显示  
# 语句中包含[], {} 或 () 括号就不需要使用多行连接符
print "one " + \
    "two " + \
    "three"

# python 中多行注释使用三个单引号(''')或三个双引号(""")
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

import sys
# 等待用户输入
input = raw_input("\nPress the enter key to exit.\n")
sys.stdout.write("你输入的参数为："+input+'\n')


# Python 中的变量赋值不需要类型声明
count = 100     #赋值整形变量
money = 123.45  #赋值浮点型变量
name  = "张三"   #字符串变量
print name
print money
print count


# 变量赋值
a = b = c = 1       #创建一个整型对象，值为1，三个变量被分配到相同的内存空间上
print a+b+c

a, b, c = 1, 2, "john"      #两个整型对象1和2的分配给变量a和b，字符串对象"john"分配给变量c
print a
del b       #删除变量
#print b     # 运行报 NameError: name 'b' is not defined
print c

