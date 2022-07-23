import pygame

class Basket():
    """模拟球篮的类"""

    def __init__(self,screen,game_settings):
        """初始化球篮的设置"""
        self.screen = screen
        self.game_settings = game_settings

        #加载球篮图像
        self.image = pygame.image.load(r'球篮.png')

        self.set_basket_position()  #设置球篮位置

    def set_basket_position(self):
        """设置球篮位置"""
        self.basket_x = self.game_settings.basket_x_initial_value
        self.basket_y = self.game_settings.basket_y
        
    def update(self):
        """移动球篮"""
        if pygame.mouse.get_pos()[0] <= self.game_settings.screen_width - self.game_settings.basket_width:
            self.basket_x= pygame.mouse.get_pos()[0]

    def draw_basket(self):
        """在指定位置绘制球篮"""
        self.screen.blit(self.image,[self.basket_x,self.basket_y])
