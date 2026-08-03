##①定义类
# ②查看帮助信息
# ③查看历史总积分
# ④创建游戏对象，开始游戏
# ⑤查看历史总积分
# todo 属性:
#  1.定义一个类属性top_score记录游戏的历史总积分
#  2.定义一个实例属性player_name记录当前游戏的玩家姓名
#  方法:
#  1.静态方法show_help显示游戏帮助信息
#  2.类方法show_all_score显示历史总积分
#  3.实例方法start_gcame开始当前玩家的游戏

class Game(object):
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print('显示游戏帮助信息')