import pygame
from Globals import GlobalsVar as Gv, GlobalsImg as Gi


class Enemy:
    def __init__(self, start_pos_x: int, start_pos_y: int, damage: int):
        self.img = Gi.enemy_image
        self.pos_x = start_pos_x
        self.pos_y = start_pos_y
        self.rotation = pygame.transform.rotate(self.img, 0)
        self.damage = damage

    def move(self, speed):
        self.pos_x -= speed

    def draw(self):
        Gv.screen.blit(self.rotation, (self.pos_x, self.pos_y))


class EnemyFabric:
    @staticmethod
    def generate(pos_x: int, pos_y: int, damage: int):
        enemy = Enemy(pos_x, pos_y, damage)
        return enemy
