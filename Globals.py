from pygame import init, font, time, image

init()

WIDTH = 1024
HEIGHT = 720
FONT = font.SysFont("Courier", 16, 1, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = time.Clock()

Texture_Image = image.load('assets/Textura.png')
Base_Image = image.load('assets/object1.png')
Enemy_Image = image.load('assets/enemy.png')
Player_Image = image.load('assets/main_character.png')
Bullet_Image = image.load('assets/object2.png')
