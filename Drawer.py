from Main_Functions import fill_background, generate_base


class Drawer:
    def __init__(self, player, enemy_list, bullet_list, health_label, time_label):
        self.player = player
        self.enemy_list = enemy_list
        self.bullet_list = bullet_list
        self.health_label = health_label
        self.time_label = time_label

    def draw_all(self):
        fill_background()
        generate_base()
        for e in self.enemy_list:
            e.draw()
        for b in self.bullet_list:
            b.draw()
        self.health_label.draw()
        self.time_label.draw()
        self.player.draw()
