from pygame import *


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
