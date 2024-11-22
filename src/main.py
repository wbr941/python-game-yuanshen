import pygame
import sys
from setting import Setting
from wendy import Wendy

class YuanShen:
    def __init__(self):
        # 初始化 Pygame 和设置
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.bg_color = self.setting.bg_color
        self.clock = pygame.time.Clock()

        # 初始化 Wendy 角色
        self.wendy = Wendy(self)
        
        # 加载开始图像
        self.start_img = pygame.image.load("pic/start.png")
        self.start_img_rect = self.start_img.get_rect()

        # 初始化淡入淡出变量
        self.alpha = 0  # 当前透明度
        self.fading_in = True # 淡入状态
        self.wait_time = 0  # 等待时间计数
        self.wait_duration = 72  # 等待的持续时间
        self.show_character = False # 是否显示角色
        self.pic_fade_out = True  # 图片淡出状态

    def handle_input(self):
        """处理用户输入，控制 Wendy 角色的移动和跳跃"""
        self.keys = pygame.key.get_pressed()  # 获取当前按下的键
        if self.keys[pygame.K_d]:
            self.wendy.move_right()  # 向右移动
        if self.keys[pygame.K_a]:
            self.wendy.move_left()  # 向左移动
        if self.keys[pygame.K_SPACE]:
            self.wendy.jump()  # 角色跳跃

    def fade_in(self):
        """处理淡入效果"""
        if self.alpha < 255:
            self.alpha += 5  # 增加透明度
        else:
            self.fading_in = False  # 淡入完成

    def wait(self):
        """处理等待逻辑"""
        self.wait_time += 1  # 增加等待时间计数

    def fade_out(self):
        """处理淡出效果"""
        if self.alpha > 0:
            self.alpha -= 5  # 减少透明度
        else:
            self.show_character = True  # 显示角色

    def _pic_fade_out(self):
        """处理开始图像的淡入淡出"""
        # 将图像缩放到屏幕大小并设置透明度
        scaled_start_img = pygame.transform.scale(self.start_img, (self.setting.screen_width, self.setting.screen_height))
        scaled_start_img.set_alpha(self.alpha)
        self.screen.blit(scaled_start_img, (0, 0))  # 绘制图像

        # 根据当前状态调用相应的处理方法
        if self.fading_in:
            self.fade_in()  # 进行淡入
        elif not self.fading_in and self.wait_time < self.wait_duration:
            self.wait()  # 进行等待
        else:
            self.fade_out()  # 进行淡出

    def run_game(self):
        """主游戏循环"""
        while True:
            self.screen.fill(self.bg_color)  # 清屏并填充背景色

            self.handle_input()  # 处理输入

            if self.show_character:
                self.wendy.blit_me()  # 如果需要，绘制角色
            
            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # 退出游戏

            if self.pic_fade_out:
                self._pic_fade_out()  # 执行淡入淡出逻辑

            pygame.display.flip()  # 刷新屏幕
            self.clock.tick(60)  # 设置帧率为60帧

# 创建游戏实例
game = YuanShen()
# 运行游戏
game.run_game()
