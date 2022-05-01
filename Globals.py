import pygame

pygame.init()


class GlobalsVar:
    WIDTH = 1024
    HEIGHT = 720
    FONT = pygame.font.SysFont("Courier", 16, 1, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    START_MENU = 0
    GAME = 1
    LOSE_MENU = 2

    FPS = pygame.time.Clock()

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


class GlobalsImg:
    Texture_Image = pygame.image.load('assets/Textura.png')
    Base_Image = pygame.image.load('assets/object1.png')
    Enemy_Image = pygame.image.load('assets/enemy.png')
    Player_Image = pygame.image.load('assets/main_character.png')
    Bullet_Image = pygame.image.load('assets/object2.png')
    Restart_Image = pygame.image.load('assets/lose_menu_button1.png')
    Background_Image = pygame.image.load('assets/start_menu_background.jpg')
    Background_Lose_Image = pygame.image.load('assets/lose_menu_background.jpg')
    Home_Image = pygame.image.load('assets/lose_menu_button2.png')
    Start_Image = pygame.image.load('assets/start_menu_button1.png')
    Exit_Image = pygame.image.load('assets/start_menu_button2.png')
