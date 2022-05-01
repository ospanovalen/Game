import pygame
from Bullet import Bullet
from Globals import GlobalsVar as Gv, GlobalsImg as Gi


class Player:
    def __init__(self, start_pos_x: int, start_pos_y: int):
        self.img = Gi.player_image
        self.pos_x = start_pos_x
        self.pos_y = start_pos_y
        self.rotation = pygame.transform.rotate(self.img, 0)

    def rotate(self, angle: float):
        self.rotation = pygame.transform.rotate(self.img, angle)

    def move_h(self, speed):
        self.pos_x += speed

    def move_v(self, speed):
        self.pos_y += speed

    def move(self, speed: float, keys_dict: dict):
        if keys_dict['right'] and self.pos_x < Gv.width:
            self.move_h(speed)
        elif keys_dict['left'] and self.pos_x > 0:
            self.move_h(-speed)

        if keys_dict['up'] and self.pos_y > 0:
            self.move_v(-speed)
        elif keys_dict['down'] and self.pos_y < Gv.height:
            self.move_v(speed)

    def draw(self):
        Gv.screen.blit(self.rotation, (self.pos_x, self.pos_y))

    def shoot(self, bullets_list: list, bullets_limit: int, angle: float):
        if len(bullets_list) < bullets_limit:
            bullets_list.append(Bullet(angle, self.pos_x, self.pos_y))
