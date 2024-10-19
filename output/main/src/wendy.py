import pygame
 
# Wendy类负责创建和管理Wendy角色的属性和行为
class Wendy:
    # 初始化方法，设置游戏屏幕和Wendy的图像
    def __init__(self,game):
        self.screen = game.screen
        self.image = pygame.image.load("pic/wendy_img.png")
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
         
     
    # 在屏幕上绘制Wendy
    def blit_me(self):
        self.screen.blit(self.image, self.rect)
 
    # 向右移动Wendy
    def move_left(self):
        self.rect.x -= 2  # 向右移动2
         
     
    # 向左移动Wendy
    def move_right(self): 
        self.rect.x += 2 # 向左移动2