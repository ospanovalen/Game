from Globals import GlobalsVar as Gi


class Button:
    def __init__(self, pos_x: float, pos_y: float, img):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = img

    def draw(self):
        Gi.screen.blit(self.img, (self.pos_x, self.pos_y))
