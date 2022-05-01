import pygame
from Button import Button
from Globals import GlobalsVar as Gv, GlobalsImg as Gi


class StartMenu:
    def __init__(self):
        self.is_active = False
        self.pos_x = 0
        self.pos_y = 0
        self.size_x = Gv.WIDTH
        self.size_y = Gv.HEIGHT
        ei = pygame.transform.scale(Gi.Exit_Image, (self.size_x // 4, self.size_y // 4))
        si = pygame.transform.scale(Gi.Start_Image, (self.size_x // 4, self.size_y // 4))
        self.start_game_button = Button(self.pos_x + self.size_x // 2 - si.get_width() / 2,
                                        self.pos_y + self.size_y // 3,
                                        si
                                        )
        self.quit_game_button = Button(self.pos_x + self.size_x // 2 - ei.get_width() / 2,
                                       self.pos_y + self.size_y * 2 // 3,
                                       ei
                                       )
        self.background = pygame.transform.scale(Gi.Background_Image, (self.size_x, self.size_y))

    def draw(self):
        Gv.SCREEN.blit(self.background, (self.pos_x, self.pos_y))
        self.start_game_button.draw()
        self.quit_game_button.draw()
