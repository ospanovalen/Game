from pygame import *
from math import cos, sin, pi
from Globals import Bullet_Image


class Bullet:
    def __init__(self, angle: float, start_pos_x: int, start_pos_y: int):
        self.img = Bullet_Image
        self.angle = angle
        self.posX = start_pos_x
        self.posY = start_pos_y
        self.rotation = transform.rotate(self.img, 360 - angle * 180 / pi)

    def move(self, speed):
        self.posX += cos(self.angle) * speed
        self.posY += sin(self.angle) * speed

    def update(self, screen):
        screen.blit(self.rotation, (self.posX, self.posY))
