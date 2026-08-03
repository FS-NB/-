# 需求：动物类，不同动物的叫声不一样

"""
1.有继承
    父类：Animal：call方法
    子类：
    子类：Duck继承Animal
2.函数重写
    子类重写父类方法

3.父类引用指向子类对象

"""


# class Animal(object):
#     def call(self):
#         print('叫你爹')
#
# class Dog(Animal):
#     def call(self):
#         print('叫！')
#
# class Duck(Animal):
#     def call(self):
#         print('来')
#
#
# #3.父类引用指向子类对象
# # 动物需要喂养
# def feed(animal):
#     animal.call()
#
# dog = Dog()
# feed(dog)
#
# duck = Duck()
# feed(duck)

# todo 需求:实现一个多态案例
#  ·定义Employee类:有work()方法
#  ·定义Programmer类:继承Employee，重写work()方法，输出"编写代码..."
#  ·定义Manager类:继承Employee，重写work()方法，输出”管理团队.."
#  ·定义company类:有start_work(employee)方法,调用employee.work()
#  ·创建对象并演示多态

class Employee(object):
    def work(self):
        print('工作')


class Programmer(Employee):
    def work(self):
        print("编写代码...")


class Manager(Employee):
    def work(self):
        print("管理团队...")


class Company(Employee):
    def start_work(self,employee):
        employee.work()
        self.work()


pro = Programmer()
mana = Manager()
com = Company()
com.start_work(pro)
com.start_work(mana)
