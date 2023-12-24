import pygame
from pygame.locals import *

# 初始化游戏
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 加载背景图片
background = pygame.image.load("background.jpg")

# 加载玩家图片
player = pygame.image.load("player.png")
player_rect = player.get_rect()
player_rect.topleft = (50, 50)

# 设定移动速度
move_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_rect.x -= move_speed
    if keys[K_RIGHT]:
        player_rect.x += move_speed
    if keys[K_UP]:
        player_rect.y -= move_speed
    if keys[K_DOWN]:
        player_rect.y += move_speed

    # 绘制背景和玩家
    screen.blit(background, (0, 0))
    screen.blit(player, player_rect)

    pygame.display.update()
    clock.tick(60)
