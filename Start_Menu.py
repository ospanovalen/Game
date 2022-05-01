import pygame
from Button import Button
from Globals import GlobalsVar as Gv, GlobalsImg as Gi


class StartMenu:
    def __init__(self):
        self.is_active = False
        self.pos_x = 0
        self.pos_y = 0
        self.size_x = Gv.width
        self.size_y = Gv.height
        ei = pygame.transform.scale(Gi.exit_image, (self.size_x // 6, self.size_y // 6))
        si = pygame.transform.scale(Gi.single_player_image, (self.size_x // 8, self.size_y // 5))
        mi = pygame.transform.scale(Gi.multi_player_image, (self.size_x // 8, self.size_y // 5))
        self.start_game_button = Button(self.pos_x + self.size_x // 3 - si.get_width() / 2,
                                        self.pos_y + self.size_y // 3,
                                        si
                                        )
        self.start_multiplayer_game_button = Button(self.pos_x + self.size_x * 2 // 3 - si.get_width() / 2,
                                                    self.pos_y + self.size_y // 3,
                                                    mi
                                                    )
        self.quit_game_button = Button(self.pos_x + self.size_x // 1.15 - ei.get_width() / 5,
                                       self.pos_y + self.size_y * 5 // 6,
                                       ei
                                       )
        self.background = pygame.transform.scale(Gi.background_image, (self.size_x, self.size_y))

    def draw(self):
        Gv.screen.blit(self.background, (self.pos_x, self.pos_y))
        self.start_game_button.draw()
        self.start_multiplayer_game_button.draw()
        self.quit_game_button.draw()
