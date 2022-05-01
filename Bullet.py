import pygame
from math import cos, sin, pi
from Globals import GlobalsVar as Gv, GlobalsImg as Gi


class Bullet:
    def __init__(self, angle: float, start_pos_x: int, start_pos_y: int):
        self.img = Gi.bullet_image
        self.angle = angle
        self.pos_x = start_pos_x
        self.pos_y = start_pos_y
        self.rotation = pygame.transform.rotate(self.img, angle)

    def move(self, speed):
        self.pos_x += cos(self.angle * pi / 180) * speed
        self.pos_y += sin(-self.angle * pi / 180) * speed

    def draw(self):
        Gv.screen.blit(self.rotation, (self.pos_x, self.pos_y))
