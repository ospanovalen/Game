from Bullet import *
from Globals import Player_Image


class Player:
    def __init__(self, start_pos_x: int, start_pos_y: int):
        self.img = Player_Image
        self.posX = start_pos_x
        self.posY = start_pos_y
        self.rotation = transform.rotate(self.img, 0)

    def rotate(self, angle: float):
        self.rotation = transform.rotate(self.img, 360 - angle)

    def move_h(self, speed):
        self.posX += speed

    def move_v(self, speed):
        self.posY += speed

    def update(self, screen):
        screen.blit(self.rotation, (self.posX, self.posY))

    def shoot(self, bullets_list: list, bullets_limit: int, angle):
        if len(bullets_list) < bullets_limit:
            bullets_list.append(Bullet(angle, self.posX, self.posY))
