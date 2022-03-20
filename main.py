from pygame import *
from math import atan2, pi
from Main_Classes import Player, EnemyFabric, TimeLabel, HealthLabel
from random import randint

init()

# set initial settings
display.set_caption("Defender")

# define constants
WIDTH = 1300
HEIGHT = 1000
FONT = font.SysFont('Courier', 16, 1, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = display.set_mode((WIDTH, HEIGHT))

# define main objects
player = Player(100, 100)
timeLabel = TimeLabel(FONT, BLUE, GREEN, 5, HEIGHT - 32)
healthLabel = HealthLabel(FONT, BLUE, RED, 5, HEIGHT - 16)

# set images
Texture_Image = image.load('Objects/Textura.png')
Base_Image = image.load('Objects/object1.png')

Bullets_List = []
Enemies_List = []
Enemy_Delay = 100
Health_Points = 100
Bullets_Limit = 2
Speed = 5

FPS = time.Clock()
Running = True

Keys_Dict = {'up': False, 'down': False, 'left': False, 'right': False}
mousePos = {'x': 0, 'y': 0}

while Running:
    # fill screen with background image
    for x in range(WIDTH // Texture_Image.get_width() + 1):
        for y in range(HEIGHT // Texture_Image.get_height() + 1):
            screen.blit(Texture_Image, (x * Texture_Image.get_width(), y * Texture_Image.get_height()))

    # generate base image
    for y in range(HEIGHT % Base_Image.get_height() // 2,
                   HEIGHT - Base_Image.get_height(),
                   Base_Image.get_height()):
        screen.blit(Base_Image, (5, y))

    # get mouse position
    mousePos['x'], mousePos['y'] = mouse.get_pos()
    angleRadian = atan2(mousePos['y'] - player.posY,
                        mousePos['x'] - player.posX)

    # player rotation
    angleDegree = angleRadian * 180 / pi
    player.rotate(angleDegree)

    # player movement
    if Keys_Dict['right'] and player.posX < WIDTH:
        player.move_h(Speed)
    elif Keys_Dict['left'] and player.posX > 0:
        player.move_h(-Speed)

    if Keys_Dict['up'] and player.posY > 0:
        player.move_v(-Speed)
    elif Keys_Dict['down'] and player.posY < HEIGHT:
        player.move_v(Speed)

    for e in event.get():
        if e.type == QUIT:
            print('Stop')
            Running = False

        # keyboard manager
        if e.type == KEYDOWN:
            if e.key == K_UP:
                Keys_Dict['up'] = True
            elif e.key == K_DOWN:
                Keys_Dict['down'] = True
            elif e.key == K_LEFT:
                Keys_Dict['left'] = True
            elif e.key == K_RIGHT:
                Keys_Dict['right'] = True

        if e.type == KEYUP:
            if e.key == K_UP:
                Keys_Dict['up'] = False
            elif e.key == K_DOWN:
                Keys_Dict['down'] = False
            elif e.key == K_LEFT:
                Keys_Dict['left'] = False
            elif e.key == K_RIGHT:
                Keys_Dict['right'] = False

        # shoot
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            player.shoot(Bullets_List, Bullets_Limit, angleRadian)

    player.update(screen)

    # bullets movement
    for bullet in Bullets_List:
        bullet.move(10)
        bullet.update(screen)

        if (bullet.posX < 0 or bullet.posX > WIDTH or
            bullet.posY < 0 or bullet.posY > HEIGHT):
            Bullets_List.remove(bullet)

    # Generate Enemy
    Enemy_Delay -= randint(0, 3)
    if Enemy_Delay < 0:
        pos_y = randint(Base_Image.get_height(), HEIGHT - Base_Image.get_height())
        Enemies_List.append(EnemyFabric.generate(WIDTH, pos_y, 5))
        Enemy_Delay = 100

    # enemy manager
    for enemy in Enemies_List:
        # enemy movement
        enemy.move(5)
        enemy.update(screen)

        # enemy beat the base
        if enemy.posX < 0 + Base_Image.get_width() // 2:
            Health_Points -= enemy.damage
            Enemies_List.remove(enemy)
            if Health_Points <= 0:
                Running = False

        enemyRect = enemy.img.get_rect()
        enemyRect.left = enemy.posX
        enemyRect.top = enemy.posY

        for bullet in Bullets_List:
            bulletRect = bullet.img.get_rect()
            bulletRect.left = int(bullet.posX)
            bulletRect.top = int(bullet.posY)
            if enemyRect.colliderect(bulletRect):
                Enemies_List.remove(enemy)
                Bullets_List.remove(bullet)

    timeLabel.update(screen)
    healthLabel.update(Health_Points, screen)

    FPS.tick(60)
    display.update()

print('Игра завершена')
quit()
