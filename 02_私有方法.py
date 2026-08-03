class Girl:
    def __init__(self, name, age):
        self.name = name
        # 将age设置为私有属性
        self.__age = age

    def __study(self):
        print('好好学习')


    def set_age(self,age):
        self.__age = age


    def get_age(self):
        return self.__age


# todo 3.构造对象并访问属性
girl = Girl('小妹', 88)
print(girl.name)
print(girl.get_age())