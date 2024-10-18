import pygame
import sys
from setting import Setting
class YuanShen:
    def __init__(self):
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.bg_color = self.setting.bg_color
        self.clock = pygame.time.Clock()
        self.start_img = pygame.image.load("pic\start.png")
        self.start_img_rect = self.start_img.get_rect()
        self.start_img_rect.center = (0,0)

    def run_game(self):
        while True:
            for event in pygame.event.get():  # 遍历所有事件
                if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                    sys.exit()
            
        
            self.screen.fill(self.bg_color)
            self.screen.blit(self.start_img,self.start_img_rect)
            pygame.display.flip()
            self.clock.tick(60)

game = YuanShen()
game.run_game()
        

