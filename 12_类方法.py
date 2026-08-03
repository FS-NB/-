class Tool():
    count = 0

    @classmethod
    def total(cls):
        print(cls.count)#Tool.count


Tool.total()