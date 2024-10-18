import pygame
import sys
from setting import Setting

pygame.init()
setting = Setting()
screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
bg_color = (255,255,255)
clock = pygame.time.Clock()
start_img = pygame.image.load("pic\start.png")
start_img_rect = start_img.get_rect()
start_img_rect.center = (0,0)
while True:
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
    
    screen.fill(bg_color)
    screen.blit(start_img,start_img_rect)
    pygame.display.flip()
    clock.tick(60)
     

