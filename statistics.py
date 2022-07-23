import pygame
import json

class Statistics():
    """统计游戏信息的类"""
    def __init__(self,screen):
        """初始化不变统计设置"""
        self.screen = screen  #初始化屏幕

        #初始化最高得分
        try:
            #“最高得分.json”存在，表示有历史记录
            with open("最高得分.json",'r') as f:
                self.highest_score = json.load(f)
        except FileNotFoundError:
            #“最高得分.json”不存在，表示无历史记录
            self.highest_score = 0
        
        self.initialize_variable_statistics_settings()  #初始化可变统计设置

    
    def initialize_variable_statistics_settings(self):
        """初始化可变统计设置"""
        self.score = 0  #初始化得分
        self.life = 5  #初始化生命
        self.game_running_logo = True  #初始化游戏运行标志

    
    def game_running_statistics(self):
        """游戏运行时的统计"""
        #绘制得分
        text = "球球接接接  游戏进行中  当前得分：" + str(self.score) + "  当前生命：" + str(self.life) +"  历史最高得分：" + str(self.highest_score) + "  按[Q]键结束游戏"
        pygame.display.set_caption(text)

        #更新最高得分
        if self.score > self.highest_score:
            self.highest_score = self.score

    
    def game_not_running_statistics(self):
        """游戏不运行时的统计"""
        #绘制得分
        text = "球球接接接  游戏结束  本局得分：" + str(self.score) + "  历史最高得分：" + str(self.highest_score) + "  按[P]键重新开始游戏"
        pygame.display.set_caption(text)
