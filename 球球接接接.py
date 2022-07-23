#导入内置模块
import pygame
import os

#导入自定义模块
from settings import Settings
from basket import Basket
from ball import Ball
from statistics import Statistics
import game_functions as gf

#准备游戏
pygame.init()  #初始化pygame
game_settings = Settings()  #设置game_settings对象以调用设置

#设置屏幕
os.environ ['SDL_VIDEO_CENTERED'] = '1'  #窗口居中
screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height)) #设置屏幕大小

pygame.mouse.set_visible(False)  #隐藏光标

game_information = Statistics(screen)  #初始化统计信息

basket = Basket(screen,game_settings)  #创建球篮
ball = Ball(screen,game_settings)  #创建球

#开始游戏
while True:
    #响应事件
    gf.chect_events(basket,ball,game_settings,game_information)
        
    #开始游戏
    if game_information.game_running_logo:
        #更新游戏对象
        gf.update_game_objects(basket,ball)
        
        #更新屏幕
        gf.update_screen(game_settings,screen,basket,ball)
    
        #计分
        gf.scoring(game_settings,basket,ball,game_information)

        #游戏运行统计
        game_information.game_running_statistics()
    
    else:
        #游戏结束统计
        game_information.game_not_running_statistics()
