class Tool(object):
    # 定义类属性，用于记录创建了多少个工具对象
    count = 0
    def __init__(self,name):
        self.name = name
        # 针对类属性做一个计数+1的操作
        Tool.count += 1


tool1 = Tool('Tou')
tool2 = Tool('ji')
tool3 = Tool('di')

print(Tool.count)