# -*- coding: UTF-8 -*-

'''
Python内置类属性
    __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
    __doc__ :类的文档字符串
    __name__: 类名
    __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
    __bases__ : 类的所有父类构成元素（包含了以个由所有父类组成的元组）
Python内置类属性调用实例如下：
'''

class Employee:
    '员工类'
    
    #类变量
    empCount = 0

    #私有变量
    __age = 0
    #被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    def __init__(self,name,salary,age):
        self.name = name
        self.salary = salary
        self.__age = age
        Employee.empCount += 1
        
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
        
    def displayEmployee(self):
        print "Name: ",self.name," ,Salary: ",self.salary," ,Age:",self.__age
        

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__



#创建 Employee 类的第一个对象
emp1 = Employee("张三",30000,13)
#创建 Employee 类的第二个对象
emp2 = Employee("李四",30000,40)
emp1.displayEmployee()
emp2.displayEmployee()

# 报错，实例不能访问私有变量
#print(emp1.__age)

print "Total Employee %d" % Employee.empCount




'''
属性操作
    getattr(obj, name[, default]) : 访问对象的属性。
    hasattr(obj,name) : 检查是否存在一个属性。
    setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
    delattr(obj, name) : 删除属性。
'''
emp1.age = 19       # 添加一个 'age' 属性
emp1.age = 20       # 修改 'age' 属性
del emp1.age        # 删除 'age' 属性

setattr(emp1, 'sex', "男")   # 如果属性（'sex'）不存在则添加，如果存在则修改
hasattr(emp1, 'sex')        # 如果存在 'sex' 属性返回 True。
getattr(emp1, 'sex')        # 返回 'sex' 属性的值
delattr(emp1, 'sex')        # 删除属性 'age'



