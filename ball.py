import pygame
import random

class Ball():
    """模拟球的类"""
    
    
    def __init__(self,screen,game_settings):
        """初始化球的设置"""
        self.screen = screen  #初始化屏幕
        self.game_settings = game_settings  #初始化游戏设置
        
        self.set_ball_position()  #设置球位置 
        
    
    def set_ball_position(self):
        """设置球位置"""
        self.ball_x = random.randint(int(self.game_settings.ball_diameter),self.game_settings.screen_width - int(self.game_settings.ball_diameter))  #设置球x位置
        self.ball_y = int(self.game_settings.ball_diameter)  #设置球y位置
    
    
    def update(self):
        """更新球的位置"""
        self.ball_y += int(self.game_settings.ball_speed)
    
        
    def draw_ball(self):
        """在指定位置绘制球"""
        pygame.draw.circle(self.screen,self.game_settings.ball_colour,[self.ball_x,self.ball_y],int(self.game_settings.ball_diameter))

