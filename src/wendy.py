import pygame

class Wendy:
    def __init__(self,game):
        self.screen = game.screen
        self.image = pygame.image.load("pic/wendy_img.png")
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        
    
    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def move_right(self,key):
        self.rect.x += 2  # 向右移动5
        
    
    def move_left(self):
        self.rect.x += 2
