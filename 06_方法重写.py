"""
1.定义一个动物类 class Animal
姓名 ，年龄

2.定义一个猫类 class Cat(Animal)

3.定义一个狗类 class Dog(Animal)
"""

"""
方法重写思路梳理：

1.父类：动物胶的方法交call
2.子类重写（覆盖）父类中的call方法
3.子类调用该方法
"""


class Animal(object):

    def eat(self):
        print('我要吃饭~~~~~！')

    def call(self):
        print('叫')


# 2.定义一个猫类 class Cat(Animal)
class Cat(Animal):
    def call(self):
        print('邪恶小鼻嘎')


# 3.定义一个狗类 class Dog(Animal)
class Dog(Animal):
    def call(self):
        print('666')

cat = Cat()
cat.eat()
cat.call()

dog = Dog()
dog.eat()
dog.call()

print(Cat.__bases__)  # 查看Cat父类
print(Dog.__bases__)  # 查看Dog父类
