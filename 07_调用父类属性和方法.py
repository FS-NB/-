"""
1.定义一个动物类 class Animal
姓名 ，年龄

2.定义一个猫类 class Cat(Animal)

3.定义一个狗类 class Dog(Animal)
"""

"""
步骤分析：
1.动物类父类：name age
2.子类同样也有name 和 age ，再增加一个
"""


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print('我要吃饭~~~~~！')

    def call(self):
        print('叫')


# 2.定义一个猫类 class Cat(Animal)
class Cat(Animal):
    def __init__(self, name, age,sex):
        super().__init__(name,age)
        self.sex = sex
    def call(self):
        print(f'{self.name}邪恶小鼻嘎')


# 3.定义一个狗类 class Dog(Animal)
class Dog(Animal):
    def __init__(self, name, age,sex):
        super(Dog,self).__init__(name,age)
        self.sex = sex
    def call(self):
        print(f'{self.name}666')

cat = Cat('天机星',18,'男')
cat.eat()
cat.call()

dog = Dog('伍六七',18,'男')
dog.eat()
dog.call()

print(Cat.__bases__)  # 查看Cat父类
print(Dog.__bases__)  # 查看Dog父类
