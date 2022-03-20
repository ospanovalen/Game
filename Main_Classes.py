from pygame import *
from math import sin, cos, pi


class Bullet:
    def __init__(self, angle: float, start_pos_x: int, start_pos_y: int):
        self.img = image.load('Objects/object2.png')
        self.angle = angle
        self.posX = start_pos_x
        self.posY = start_pos_y
        self.rotation = transform.rotate(self.img, 360 - angle * 180 / pi)

    def move(self, speed):
        self.posX += cos(self.angle) * speed
        self.posY += sin(self.angle) * speed

    def update(self, screen):
        screen.blit(self.rotation, (self.posX, self.posY))


class Player:
    def __init__(self, start_pos_x: int, start_pos_y: int):
        self.img = image.load('Objects/main_character.png')
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


class Enemy:
    def __init__(self, start_pos_x: int, start_pos_y: int, damage: int):
        self.img = image.load('Objects/enemy.png')
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


class Label:
    def __init__(self, font_s: font, color_back, color_font, pos_x, pos_y):
        self.font = font_s
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color_back = color_back
        self.color_font = color_font
        self.img = self.font.render('', True, color_back, color_font)


class TimeLabel(Label):
    def update(self, screen):
        self.img = self.font.render(
            'Time: ' +
            str(round((time.get_ticks() / 1000), 1)),
            True,
            self.color_font,
            self.color_back
        )
        screen.blit(self.img, (self.pos_x, self.pos_y))


class HealthLabel(Label):
    def update(self, hp, screen):
        self.img = self.font.render(
            'Health: ' + str(hp) + '%',
            True,
            self.color_font,
            self.color_back
        )
        screen.blit(self.img, (self.pos_x, self.pos_y))
