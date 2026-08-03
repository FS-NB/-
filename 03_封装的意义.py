class Girl:
    def __init__(self, name, age):
        self.name = name
        # 将age设置为私有属性
        self.__age = age

    def set_age(self,age):
        if age >= 0 and age <= 100:
            self.__age = age
        else:
            print('qnmd,你年龄出bug了')

    def get_age(self):
        return self.__age


# todo 3.构造对象并访问属性
girl = Girl('小妹', 88)
print(girl.name)
girl.set_age(18)
print(girl.get_age())