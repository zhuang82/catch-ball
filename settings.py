class Settings():
    """存储游戏所有设置"""

    def __init__(self):
        """初始化不可变游戏设置"""

        #屏幕设置
        self.screen_width = 1200  #屏幕宽度
        self.screen_height = 600  #屏幕高度
        self.background_color = (200,200,200)  #背景颜色

        #球篮设置
        self.basket_width = 150  #球篮宽
        self.basket_height = 100  #球篮高
        self.basket_x_initial_value = (self.screen_width - self.basket_width) / 2  #球篮x位置初始值
        self.basket_y = self.screen_height - self.basket_height  #球篮y位置
        
        #球设置
        self.ball_colour = (255,0,0)  #球颜色

        #加快速度
        self.pick_up_speed = 1.1

        #初始化可变设置
        self.initialize_variable_settings()


    def initialize_variable_settings(self):
        """初始化可变设置"""
        self.ball_speed = 1  #球速度
        self.ball_diameter = 50  #球半径


    def upadte_settings(self):
        """更新设置"""
        self.ball_speed *= self.pick_up_speed  #更新球速度
        self.ball_diameter /= self.pick_up_speed  #更新球半径 
