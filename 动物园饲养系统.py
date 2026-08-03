"""
### 题目背景

某动物园需要开发一套动物饲养管理系统，用于记录不同动物的信息以及饲养员给动物喂食的操作。请你使用面向对象的思想完成以下设计。
"""


# todo **（一）动物类（父类）`Animal`**
#  属性
#  - `name`：动物名称（由外部传入）
#  - `age`：动物年龄（由外部传入）
#  - `__health`：健康值（私有属性，默认 `100`）
#  方法：
#  - `eat()`：打印 `"{name} 正在吃东西..."`
#  - `sleep()`：打印 `"{name} 正在睡觉..."`
#  - `get_health()`：获取健康值（公有方法，返回 `__health`）
#  - `set_health(value)`：设置健康值，范围限制在 `0~100` 之间（公有方法）
#  - `show_info()`：打印动物的基本信息（名称、年龄、健康值）
#  - `__str__()`：返回动物的完整信息字符串

class Animal(object):
    #  属性
    #  - `name`：动物名称（由外部传入）
    #  - `age`：动物年龄（由外部传入）
    #  - `__health`：健康值（私有属性，默认 `100`）
    #     - 类属性 `total_animals`：记录创建的动物总数（每创建一个动物 `+1`）
    total_animals = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__health = 100

    #  - `eat()`：打印 `"{name} 正在吃东西..."`
    def eat(self):
        print(f"{self.name} 正在吃东西...")

    #  - `sleep()`：打印 `"{name} 正在睡觉..."`
    def sleep(self):
        print(f'"{self.name} 正在睡觉..."')

    #  - `get_health()`：获取健康值（公有方法，返回 `__health`）
    def get_health(self):
        return self.__health

    #  - `set_health(value)`：设置健康值，范围限制在 `0~100` 之间（公有方法）
    def set_health(self, value):
        if 0 < value <= 100:
            self.__health = value
        else:
            return '你有病吧'

    #  - `show_info()`：打印动物的基本信息（名称、年龄、健康值）
    def show_info(self):
        print(f'打印动物的基本信息（名称{self.name}、年龄{self.age}、健康值{self.get_health()}）')

    #  - `__str__()`：返回动物的完整信息字符串
    def __str__(self):
        return self.show_info()

    # 类方法
    # `show_total()`：打印
    # `"动物园共有 {total_animals} 只动物"`
    @classmethod
    def show_total(cls):
        print(f'动物园共有 {cls.total_animals} 只动物')

#     - 静态方法 `is_healthy(health)`：判断健康值是否大于等于 `60`，返回 `True/False`
    @staticmethod
    def is_healthy(health):
        if health >= 60:
            return True
        else:
            return False


# todo 二）子类 `Dog`（继承 `Animal`）**
#  新增属性：
#  - `breed`：品种（由外部传入）
#  重写方法：
#  - `eat()`：打印 `"{name} 正在啃骨头，好香啊！"`，同时健康值 `+2`（不超过上限）
#  - 新增 `guard()` 方法：打印 `"{name} 正在看家护院！"`

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name,age)
        self.breed = breed

    # 重写方法：
    # #  - `eat()`：打印 `"{name} 正在啃骨头，好香啊！"`，同时健康值 `+2`（不超过上限）
    def eat(self):
        print(f'{self.name} 正在啃骨头，好香啊！')
        self.set_health(self.get_health() + 2)
        if self.get_health() > 100:
            self.set_health(100)

        #     #  - 新增 `guard()` 方法：打印 `"{name} 正在看家护院！"`

    def guard(self):
        print(f"{self.name} 正在看家护院！")


# todo **（三）子类 `Cat`（继承 `Animal`）**
#  新增属性：
#  - `color`：毛色（由外部传入）
#  重写方法：
#  - `eat()`：打印 `"{name} 正在吃小鱼干，真美味！"`，同时健康值 `+2`（不超过上限）
#  - 新增 `catch_mouse()` 方法：打印 `"{name} 正在抓老鼠！"`，健康值 `-5`（不低于下限）

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    # 重写方法：
    # - `eat()`：打印 `"{name} 正在吃小鱼干，真美味！"`，同时健康值 `+2`（不超过上限）
    def eat(self):
        print(f'{self.name} 正在吃小鱼干，真美味！')
        self.set_health(self.get_health() + 2)

        #  - 新增 `catch_mouse()` 方法：打印 `"{name} 正在抓老鼠！"`，健康值 `-5`（不低于下限）

    def catch_mouse(self):
        print(f"{self.name} 正在抓老鼠！")
        self.set_health(self.get_health() - 5)


# todo **（四）饲养员类 `Keeper`**
#  属性：
#   - `name`：饲养员姓名（由外部传入）
#   - `__animals`：负责的动物列表（私有属性，默认为空列表）
#   方法：
#   - `add_animal(animal)`：添加一只动物到管理列表
#   - `remove_animal(name)`：根据名称移除动物（如果存在）
#   - `feed_all()`：遍历所有动物，调用它们的 `eat()` 方法
#   - `show_all()`：遍历所有动物，调用它们的 `show_info()` 方法
#   - `get_animal_count()`：返回当前管理的动物总数（类外部可调用）

class Keeper(object):
    def __init__(self, name):
        self.name = name
        self.__animals = []

#   - `add_animal(animal)`：添加一只动物到管理列表
    def add_animal(self,animal):
        Animal.total_animals += 1
        self.__animals.append(animal)

#   - `remove_animal(name)`：根据名称移除动物（如果存在）
    def remove_animal(self,name):
        self.__animals.remove(name)

#   - `feed_all()`：遍历所有动物，调用它们的 `eat()` 方法
    def feed_all(self):
        for i in self.__animals:
            i.eat()

#   - `show_all()`：遍历所有动物，调用它们的 `show_info()` 方法
    def show_all(self):
        for i in self.__animals:
            i.show_info()

#   - `get_animal_count()`：返回当前管理的动物总数（类外部可调用）
    def get_animal_count(self):
        return len(self.__animals)

# 创建 `Dog` 对象：`"旺财"`，`3` 岁，品种 `"金毛"
dog = Dog('旺财',3,"金毛")

# 创建 `Cat` 对象：`"咪咪"`，`2` 岁，毛色 `"橘色"`
cat = Cat("cnm",2,"橘色")

# 创建饲养员 `"老王"`
keeper = Keeper("老王")

# 饲养员添加上述两只动物
keeper.add_animal(dog)
keeper.add_animal(cat)

# 调用 `show_all()` 查看所有动物信息
keeper.show_all()

# 调用 `feed_all()` 给所有动物喂食
keeper.feed_all()

# 再次调用 `show_all()` 查看喂食后的状态
keeper.show_all()

# 让咪咪抓一次老鼠，再查看咪咪的健康值（使用 `get_health()`）
cat.catch_mouse()
print(cat.get_health())

# 调用 `Animal.show_total()` 查看动物总数
Animal.show_total()

# 调用 `Animal.is_healthy(75)` 测试静态方法
print(Animal.is_healthy(75))