"""
1.定义一个动物类 class Animal
姓名 ，年龄

2.定义一个猫类 class Cat(Animal)

3.定义一个狗类 class Dog(Animal)
"""

# 1.定义一个动物类 class Animal
# 姓名 ，年龄
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s is eating' % self.name)



# 2.定义一个猫类 class Cat(Animal)
class Cat(Animal):
    pass


# 3.定义一个狗类 class Dog(Animal)
class Dog(Animal):
    pass

cat = Cat()
cat.eat()

dog = Dog()
dog.eat()

print(cat.__bases__)    #查看cat父类
print(dog.__bases__)    #查看dog父类