from pygame import *
from Globals import Enemy_Image


class Enemy:
    def __init__(self, start_pos_x: int, start_pos_y: int, damage: int):
        self.img = Enemy_Image
        self.posX = start_pos_x
        self.posY = start_pos_y
        self.rotation = transform.rotate(self.img, 0)
        self.damage = damage

    def move(self, speed):
        self.posX -= speed

    def update(self, screen):
        screen.blit(self.rotation, (self.posX, self.posY))


class EnemyFabric:
    @staticmethod
    def generate(pos_x: int, pos_y: int, damage: int):
        enemy = Enemy(pos_x, pos_y, damage)
        return enemy
