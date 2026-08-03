"""
需求： 定义父类Father，定义父类Mother，定义一个子类child

分析步骤：
1.定义父类Father
2.定义父类Mother
3.定义一个子类child

"""

# 1.定义父类Father
# class Father(object):
#     #会赚钱
#     def make_money(self):
#         print('爸爸有钱，有别墅，过来')
# # 2.定义父类Mother
# class Mother(object):
#     def cook(self):
#         print('做饭好吃')
# # 3.定义一个子类child
# class Child(Father,Mother):
#     pass
#
# #4.测试
# child = Child()
# child.make_money()
# child.cook()
#
# # 继承顺序
# print(Child.__mro__)

"""
需求:定义一个Person类和Student类
1.Person类:有name和age属性，有eat()和sleep()方法
2.Student类:继承Person类，新增score属性，重写__str_()方法显示完整信息
3.使用superO调用父类的_init_()
4.扩充:定义一个老师类:有上课的方法，也有name和age属性
"""

# 1.Person类:有name和age属性，有eat()和sleep()方法
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('我要吃饭~~~！')

    def sleep(self):
        print('碎觉碎觉，小命要紧')

#   2.Student类:继承Person类，新增score属性，重写__str_()方法显示完整信息
class Student(Person):
    def __init__(self, name, age,score):
        # 3.使用superO调用父类的_init_()
        super().__init__(name,age)
        self.score = score

    def __str__(self):
        return f'名字{self.name}，年龄{self.age}，成绩{self.score}'

# 4.扩充:定义一个老师类:有上课的方法，也有name和age属性
class Teacher(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def class_begin(self):
        print('上课')

stu = Student('xiaoshaui',18,'nan')
print(stu)
stu.eat()
stu.sleep()

teach = Teacher('cxiaoshaui',18)
teach.class_begin()