class game(object):
    top_score = 0

    @staticmethod
    def show_help():
        print("游戏帮助")
    @classmethod
    def game_method(cls):
        print("历史最高分为%d" % cls.top_score)
    def __init__(self,name):
        self.name = name
    def player_name(self):
        print("开始游戏")
game.show_help()
game.game_method()
wo = game()
