import pygame
from Button import Button
from Globals import GlobalsVar as Gv, GlobalsImg as Gi


class LoseMenu:
    def __init__(self):
        self.is_active = False
        self.pos_x = Gv.WIDTH // 10
        self.pos_y = Gv.HEIGHT // 10
        self.size_x = Gv.WIDTH * 8 // 10
        self.size_y = Gv.HEIGHT * 8 // 10
        ri = pygame.transform.scale(Gi.Restart_Image, (self.size_x * 9 // 10, self.size_y // 4))
        ei = pygame.transform.scale(Gi.Exit_Image, (self.size_x // 3, self.size_y // 5))
        hi = pygame.transform.scale(Gi.Home_Image, (self.size_x // 3, self.size_y // 5))
        self.restart_game_button = Button(self.pos_x + self.size_x // 8,
                                          self.pos_y + self.size_y // 2,
                                          ri
                                          )
        self.quit_game_button = Button(self.pos_x + self.size_x * 7 // 8 - ei.get_width(),
                                       self.pos_y + self.size_y * 3 // 4,
                                       ei
                                       )
        self.home_button = Button(self.pos_x + self.size_x // 8,
                                  self.pos_y + self.size_y * 3 // 4,
                                  hi
                                  )
        self.background = pygame.transform.scale(Gi.Background_Lose_Image, (self.size_x, self.size_y))

    def draw(self):
        Gv.SCREEN.blit(self.background, (self.pos_x, self.pos_y))
        self.restart_game_button.draw()
        self.quit_game_button.draw()
        self.home_button.draw()
