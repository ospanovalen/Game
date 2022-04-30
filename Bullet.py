import pygame
from math import cos, sin, pi
from Globals import GlobalsVar as Gv, GlobalsImg as Gi


class Bullet:
    def __init__(self, angle: float, start_pos_x: int, start_pos_y: int):
        self.img = Gi.Bullet_Image
        self.angle = angle
        self.pos_x = start_pos_x
        self.pos_y = start_pos_y
        self.rotation = pygame.transform.rotate(self.img, 360 - angle * 180 / pi)

    def move(self, speed):
        self.pos_x += cos(self.angle) * speed
        self.pos_y += sin(self.angle) * speed

    def draw(self):
        Gv.SCREEN.blit(self.rotation, (self.pos_x, self.pos_y))
