import pygame
import sys
from setting import Setting

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
        # 加载开始图像
        self.start_img = pygame.image.load("pic\start.png")
        # 获取图像矩形对象
        self.start_img_rect = self.start_img.get_rect()
        # 将图像居中放置在起始位置
        self.start_img_rect.center = (0, 0)

    def run_game(self):
        # 游戏主循环
        while True:
            # 遍历所有事件
            for event in pygame.event.get():
                # 如果单击关闭窗口，则退出
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # 填充背景颜色
            self.screen.fill(self.bg_color)
            # 在屏幕上绘制开始图像
            self.screen.blit(self.start_img, self.start_img_rect)
            # 更新屏幕显示
            pygame.display.flip()
            # 控制游戏帧率为60帧每秒
            self.clock.tick(60)

# 创建游戏实例
game = YuanShen()
# 运行游戏
game.run_game()
