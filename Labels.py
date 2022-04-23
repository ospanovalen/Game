import pygame
from Globals import GlobalsVar as Gv


class Label:
    def __init__(self, font_s: pygame.font, color_back, color_font, pos_x, pos_y):
        self.font = font_s
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color_back = color_back
        self.color_font = color_font
        self.img = self.font.render('', True, color_back, color_font)


class TimeLabel(Label):
    def update(self):
        self.img = self.font.render(
            'Time: ' +
            str(round((pygame.time.get_ticks() / 1000), 1)),
            True,
            self.color_font,
            self.color_back
        )
        Gv.SCREEN.blit(self.img, (self.pos_x, self.pos_y))


class HealthLabel(Label):
    def update(self, hp):
        self.img = self.font.render(
            'Health: ' + str(hp) + '%',
            True,
            self.color_font,
            self.color_back
        )
        Gv.SCREEN.blit(self.img, (self.pos_x, self.pos_y))
