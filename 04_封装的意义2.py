class Girl:
    def __wake(self):
        print("qichuang")

    def __brush(self):
        print("刷牙")

    def __wash(self):
        print("吸收")

    def eat(self):
        self.__wake()
        self.__brush()
        self.__wash()
        print("吃饭")


girl = Girl()
girl.eat()
