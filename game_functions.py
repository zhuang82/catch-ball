import pygame
from sys import exit
from time import sleep
import json


def new_game(basket,ball,game_settings,game_information):
    """创建新游戏"""
    basket.set_basket_position()  #创建球篮
    ball.set_ball_position()  #创建球
    game_settings.initialize_variable_settings()  #恢复设置
    game_information.initialize_variable_statistics_settings()  #恢复统计信息


def chect_events(basket,ball,game_settings,game_information):
    """响应事件"""
    for event in pygame.event.get():
        #响应鼠标退出事件
        if event.type == pygame.QUIT:  
            #将最高分写入文件
            with open("最高得分.json",'w') as f:
                json.dump(game_information.highest_score,f)
            
            #退出
            exit()  
        
        #响应键盘事件
        elif event.type == pygame.KEYDOWN:
            #按[P]键开始游戏
            if (event.key == pygame.K_p) and (not game_information.game_running_logo):
                new_game(basket,ball,game_settings,game_information)
                game_information.game_running_logo = True
                
            #按[Q]键结束游戏
            elif (event.key == pygame.K_q) and (game_information.game_running_logo):
                game_information.game_running_logo = False


def update_game_objects(basket,ball):
    """更新游戏对象"""
    basket.update()  #移动球篮
    ball.update()  #移动球篮


def update_screen(game_settings,screen,basket,ball):
    """更新屏幕"""
    #设置背景颜色
    screen.fill(game_settings.background_color)  
    
    basket.draw_basket()  #绘制球篮 
    ball.draw_ball()  #绘制球

    #刷新屏幕
    pygame.display.update()


def scoring(game_settings,basket,ball,game_information):
    """计分"""
    #检测碰撞
    if ball.ball_y >= game_settings.screen_height - game_settings.ball_diameter - game_settings.basket_height:
        #接到球
        if (ball.ball_x >= basket.basket_x) and (ball.ball_x + game_settings.ball_diameter <= basket.basket_x + game_settings.basket_width):
            game_settings.upadte_settings()
            ball.set_ball_position()
            game_information.score += 1
        
        #未接到球
        else:
            sleep(0.5)
            game_settings.initialize_variable_settings()
            basket.set_basket_position()
            ball.set_ball_position()
            game_information.life -= 1
    
    #游戏结束
    if game_information.life == 0:
        game_information.game_running_logo = False