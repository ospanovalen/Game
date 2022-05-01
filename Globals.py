import pygame

pygame.init()


class GlobalsVar:
    width = 1024
    height = 720
    font = pygame.font.SysFont("Courier", 16, 1, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    start_pos_1_x = 100
    start_pos_1_y = 100
    start_pos_2_x = 100
    start_pos_2_y = height - 100
    start_menu = 0
    game = 1
    lose_menu = 2
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))


class GlobalsImg:
    texture_image = pygame.image.load('assets/texture2.jpg')
    base_image = pygame.image.load('assets/castle1.png')
    enemy_image = pygame.image.load('assets/enemy2.png')
    player_image = pygame.image.load('assets/attack3.png')
    bullet_image = pygame.image.load('assets/bullet2.png')
    restart_image = pygame.image.load('assets/replay.png')
    background_image = pygame.image.load('assets/start_menu_background.jpg')
    background_lose_image = pygame.image.load('assets/lose_menu_background1.jpg')
    home_image = pygame.image.load('assets/lose_menu_button4.png')
    start_image = pygame.image.load('assets/start_menu_button1.png')
    single_player_image = pygame.image.load('assets/single.png')
    multi_player_image = pygame.image.load('assets/multi.png')
    exit_image = pygame.image.load('assets/start_menu_button2.png')
