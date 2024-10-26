import pygame
import sys
from setting import Setting
from wendy import Wendy

class YuanShen:
    def __init__(self):
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.bg_color = self.setting.bg_color
        self.clock = pygame.time.Clock()
        self.wendy = Wendy(self)  # 确保 Wendy 对象正常创建
        self.start_img = pygame.image.load("pic/start.png")
        self.start_img_rect = self.start_img.get_rect()

        # 初始化透明度变量和状态
        self.alpha = 0  # 透明度初始值
        self.fading_in = True  # 初始状态为淡入
        self.wait_time = 0  # 等待时间计数
        self.wait_duration = 72  # 设置等待的帧数（例如 120 帧约为 2秒）
        self.show_character = False  # 添加角色显示状态标志
    
    def _pic_fade_out(self):
        # 图片淡出效果
        # 设置图像透明度
        # 将图像调整为屏幕大小
        scaled_start_img = pygame.transform.scale(self.start_img, (self.setting.screen_width, self.setting.screen_height))
            
            # 填充背景颜色
        self.screen.fill(self.bg_color)

        scaled_start_img.set_alpha(self.alpha)
        self.screen.blit(scaled_start_img, (0, 0))
            
            # 只有在标志位为 True 时才绘制角色
        if self.show_character:
            self.wendy.blit_me()  # 如果需要绘制 Wendy

            # 淡入和淡出逻辑
        if self.fading_in:
            if self.alpha < 255:
                self.alpha += 5  # 每帧透明度增加
            else:
                self.fading_in = False  # 结束淡入，开始等待
        elif not self.fading_in and self.wait_time < self.wait_duration:
            self.wait_time += 1  # 增加等待时间计数
        else:
            if self.alpha > 0:
                self.alpha -= 5  # 每帧透明度降低
            else:
                self.show_character = True  # 透明度为0时显示角色
    def run_game(self):
        while True:
            self.keys = pygame.key.get_pressed()
            # 控制 Wendy 移动
            if self.keys[pygame.K_d]:
                self.wendy.move_right() 
            if self.keys[pygame.K_a]:
                self.wendy.move_left() 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                     
            self._pic_fade_out()
            

            pygame.display.flip()
            self.clock.tick(60)

# 创建游戏实例
game = YuanShen()
# 运行游戏
game.run_game()
