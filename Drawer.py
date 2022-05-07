from Main_Functions import fill_background, generate_base


class Drawer:
    def __init__(self, player_1, player_2, enemy_list, bullet_list_1, bullet_list_2, health_label, time_label):
        self.player_1 = player_1
        self.player_2 = player_2
        self.enemy_list = enemy_list
        self.bullet_list_1 = bullet_list_1
        self.bullet_list_2 = bullet_list_2
        self.health_label = health_label
        self.time_label = time_label

    def draw_all(self, multiplayer):
        fill_background()
        generate_base()
        for e in self.enemy_list:
            e.draw()
        for b in self.bullet_list_1:
            b.draw()
        self.health_label.draw()
        self.time_label.draw()
        self.player_1.draw()
        if multiplayer:
            for b in self.bullet_list_2:
                b.draw()
            self.player_2.draw()
