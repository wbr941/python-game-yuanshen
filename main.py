import pygame

# 初始化 Pygame
pygame.init()

# 游戏窗口的尺寸
WIDTH = 800
HEIGHT = 600

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 角色类
class Character:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# 加载背景图片
background = pygame.image.load("pic/background.png")  # 根据实际存储位置修改文件路径

# 获取背景图片的原始尺寸和窗口尺寸
bg_width, bg_height = background.get_size()
window_width, window_height = screen.get_size()

# 计算缩放比例，以适配窗口尺寸
scale_x = window_width / bg_width
scale_y = window_height / bg_height

# 缩放背景图片
background = pygame.transform.scale(background, (window_width, window_height))

# 加载角色图像
character_image = pygame.image.load("pic/character.png")  # 根据实际存储位置修改文件路径

# 实例化角色对象
character = Character(100, 100, character_image)

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 角色移动逻辑
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        character.move(1, 0)
    if keys[pygame.K_UP]:
        character.move(0, -1)
    if keys[pygame.K_DOWN]:
        character.move(0, 1)
    
    # 绘制背景
    screen.blit(background, (0, 0))
    
    # 绘制角色
    character.draw(screen)
    
    # 刷新屏幕
    pygame.display.flip()

# 退出 Pygame
import pygame

# 初始化 Pygame
pygame.init()

# 游戏窗口的尺寸
WIDTH = 800
HEIGHT = 600

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 角色类
class Character:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# 加载背景图片
background = pygame.image.load("pic/background.png")  # 根据实际存储位置修改文件路径

# 获取背景图片的原始尺寸和窗口尺寸
bg_width, bg_height = background.get_size()
window_width, window_height = screen.get_size()

# 计算缩放比例，以适配窗口尺寸
scale_x = window_width / bg_width
scale_y = window_height / bg_height

# 缩放背景图片
background = pygame.transform.scale(background, (window_width, window_height))

# 加载角色图像
character_image = pygame.image.load("pic/character.png")  # 根据实际存储位置修改文件路径

# 实例化角色对象
character = Character(100, 100, character_image)

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 角色移动逻辑
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        character.move(1, 0)
    if keys[pygame.K_UP]:
        character.move(0, -1)
    if keys[pygame.K_DOWN]:
        character.move(0, 1)
    
    # 绘制背景
    screen.blit(background, (0, 0))
    
    # 绘制角色
    character.draw(screen)
    
    # 刷新屏幕
    pygame.display.flip()

# 退出 Pygame
pygame.quit()