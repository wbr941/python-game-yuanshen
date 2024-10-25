import pygame
import sys
from setting import Setting
from wendy import Wendy

class YuanShen:
    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 加载设置
        self.setting = Setting()
        # 创建游戏窗口，并设置其宽度和高度
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        # 设置背景颜色
        self.bg_color = self.setting.bg_color
        # 创建时钟对象以控制游戏帧率
        self.clock = pygame.time.Clock()
        # 创建Wendy对象
        self.wendy = Wendy(self)
        # 加载开始图像
        self.start_img = pygame.image.load("pic/start.png")
        # 获取图像矩形（未调整大小）
        self.start_img_rect = self.start_img.get_rect()
        
        # 初始化透明度变量
        self.alpha = 0  # 透明度初始值

    def run_game(self):
        # 游戏主循环
        while True:
            # 遍历所有事件
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_d]:
                self.wendy.move_right() 
            if self.keys[pygame.K_a]:
                self.wendy.move_left() 
            for event in pygame.event.get():
                # 如果单击关闭窗口，则退出
                if event.type == pygame.QUIT:
                    sys.exit()
                     
            # 将图像调整为屏幕大小
            scaled_start_img = pygame.transform.scale(self.start_img, (self.setting.screen_width, self.setting.screen_height))
            
            # 填充背景颜色
            self.screen.fill(self.bg_color)

            # 设置图像透明度
            scaled_start_img.set_alpha(self.alpha)
            # 在屏幕上绘制缩放后的开始图像，从左上角绘制
            self.screen.blit(scaled_start_img, (0, 0))  
            self.wendy.blit_me()

            # 更新透明度，以实现淡入效果
            if self.alpha < 255:
                self.alpha += 5  # 每帧增加透明度
                if self.alpha > 255:
                    self.alpha = 255  # 确保透明度不超过255

            # 更新屏幕显示
            pygame.display.flip()
            # 控制游戏帧率为60帧每秒
            self.clock.tick(60)

# 创建游戏实例
game = YuanShen()
# 运行游戏
game.run_game()
