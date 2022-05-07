import pygame
from Button import Button
from Globals import GlobalsVar as Gv, GlobalsImg as Gi


class LoseMenu:
    def __init__(self):
        self.is_active = False
        self.pos_x = 0
        self.pos_y = 0
        self.size_x = Gv.width
        self.size_y = Gv.height
        ri = pygame.transform.scale(Gi.restart_image, (self.size_x // 3, self.size_y // 5))
        ei = pygame.transform.scale(Gi.exit_image, (self.size_x // 6, self.size_y // 6))
        hi = pygame.transform.scale(Gi.home_image, (self.size_x // 5.8, self.size_y // 5.8))
        self.restart_game_button = Button(self.pos_x + self.size_x // 3,
                                          self.pos_y + self.size_y // 3,
                                          ri
                                          )
        self.quit_game_button = Button(self.pos_x + self.size_x // 1.15 - ei.get_width() / 5,
                                       self.pos_y + self.size_y * 5 // 6,
                                       ei
                                       )
        self.home_button = Button(self.pos_x + self.size_x // 1.5,
                                  self.pos_y + self.size_y * 4.8 // 5.8,
                                  hi
                                  )
        self.background = pygame.transform.scale(Gi.background_lose_image, (self.size_x, self.size_y))

    def draw(self):
        Gv.screen.blit(self.background, (self.pos_x, self.pos_y))
        self.restart_game_button.draw()
        self.quit_game_button.draw()
        self.home_button.draw()
