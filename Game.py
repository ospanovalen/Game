import pygame
from Globals import GlobalsVar as Gv, GlobalsImg as Gi
from Labels import TimeLabel, HealthLabel
from Enemies import EnemyFabric
from Player import Player
from math import atan2, pi
from random import randint
import Main_Functions as Mf
from Start_Menu import StartMenu
from Lose_Menu import LoseMenu
from Drawer import Drawer


class Game:
    def __init__(self):
        pass

    @staticmethod
    def start_game():
        # set game name
        pygame.display.set_caption("Tower Defence")

        # define main objects
        player_1 = Player(Gv.start_pos_1_x, Gv.start_pos_1_y)
        player_2 = Player(Gv.start_pos_2_x, Gv.start_pos_2_y)
        time_label = TimeLabel(Gv.font, Gv.blue, Gv.green, 5, Gv.height - 32)
        health_label = HealthLabel(Gv.font, Gv.blue, Gv.red, 5, Gv.height - 16)

        bullets_list_1 = []
        bullets_list_2 = []
        enemies_list = []
        enemy_delay = 100
        bullets_limit = 2
        speed = 4
        damage = 5
        state = Gv.start_menu

        keys_dict_1 = {'up': False, 'down': False, 'left': False, 'right': False}
        keys_dict_2 = {'up': False, 'down': False, 'left': False, 'right': False}
        mouse_pos = {'x': False, 'y': False}

        start_menu = StartMenu()
        lose_menu = LoseMenu()

        drawer = Drawer(player_1, player_2, enemies_list, bullets_list_1, bullets_list_2, health_label, time_label)

        is_beginning = True
        multiplayer = False
        running = True

        while running:
            # get mouse position
            mouse_pos['x'], mouse_pos['y'] = pygame.mouse.get_pos()
            left_click = False
            shoot_1 = False
            shoot_2 = False

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    print('Stop')
                    running = False

                # keyboard manager
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        keys_dict_1['up'] = True
                    elif e.key == pygame.K_DOWN:
                        keys_dict_1['down'] = True
                    elif e.key == pygame.K_LEFT:
                        keys_dict_1['left'] = True
                    elif e.key == pygame.K_RIGHT:
                        keys_dict_1['right'] = True

                    if e.key == pygame.K_w:
                        keys_dict_2['up'] = True
                    elif e.key == pygame.K_s:
                        keys_dict_2['down'] = True
                    elif e.key == pygame.K_a:
                        keys_dict_2['left'] = True
                    elif e.key == pygame.K_d:
                        keys_dict_2['right'] = True

                    if e.key == pygame.K_RCTRL:
                        shoot_1 = True
                    if e.key == pygame.K_LCTRL:
                        shoot_2 = True

                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_UP:
                        keys_dict_1['up'] = False
                    elif e.key == pygame.K_DOWN:
                        keys_dict_1['down'] = False
                    elif e.key == pygame.K_LEFT:
                        keys_dict_1['left'] = False
                    elif e.key == pygame.K_RIGHT:
                        keys_dict_1['right'] = False

                    if e.key == pygame.K_w:
                        keys_dict_2['up'] = False
                    elif e.key == pygame.K_s:
                        keys_dict_2['down'] = False
                    elif e.key == pygame.K_a:
                        keys_dict_2['left'] = False
                    elif e.key == pygame.K_d:
                        keys_dict_2['right'] = False

                # shoot
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    left_click = True

            if state == Gv.game:
                if start_menu.is_active:
                    start_menu.is_active = False
                if lose_menu.is_active:
                    lose_menu.is_active = False
                if is_beginning:
                    health_points = 100
                    player_1.pos_x = Gv.start_pos_1_x
                    player_1.pos_y = Gv.start_pos_1_y
                    if multiplayer:
                        player_2.pos_x = Gv.start_pos_2_x
                        player_2.pos_y = Gv.start_pos_2_y
                    is_beginning = False

                # player rotation
                angle_1 = Mf.get_angle(keys_dict_1)
                if multiplayer:
                    angle_2 = Mf.get_angle(keys_dict_2)

                player_1.rotate(angle_1)
                player_1.move(speed, keys_dict_1)
                if shoot_1:
                    player_1.shoot(bullets_list_1, bullets_limit, angle_1)

                if multiplayer:
                    player_2.rotate(angle_2)
                    player_2.move(speed, keys_dict_2)
                    if shoot_2:
                        player_2.shoot(bullets_list_2, bullets_limit, angle_2)

                # bullets movement
                for bullet in bullets_list_1:
                    bullet.move(speed * 2)

                    if (bullet.pos_x < 0 or bullet.pos_x > Gv.width or
                            bullet.pos_y < 0 or bullet.pos_y > Gv.height):
                        bullets_list_1.remove(bullet)

                for bullet in bullets_list_2:
                    bullet.move(speed * 2)

                    if (bullet.pos_x < 0 or bullet.pos_x > Gv.width or
                            bullet.pos_y < 0 or bullet.pos_y > Gv.height):
                        bullets_list_2.remove(bullet)

                # generate Enemy
                enemy_delay -= randint(0, 3)
                if enemy_delay < 0:
                    pos_y = randint(Gi.base_image.get_height(), Gv.height - Gi.base_image.get_height())
                    enemies_list.append(EnemyFabric.generate(Gv.width, pos_y, damage))
                    enemy_delay = 100

                # enemy manager
                for enemy in enemies_list:
                    # enemy movement
                    enemy.move(speed)

                    # enemy beat the base
                    if enemy.pos_x < 0 + Gi.base_image.get_width() // 2:
                        health_points -= enemy.damage
                        enemies_list.remove(enemy)
                        if health_points <= 0:
                            enemies_list.clear()
                            state = Gv.lose_menu

                    enemy_rect = enemy.img.get_rect()
                    enemy_rect.left = enemy.pos_x
                    enemy_rect.top = enemy.pos_y

                    for bullet in bullets_list_1:
                        bullet_rect = bullet.img.get_rect()
                        bullet_rect.left = int(bullet.pos_x)
                        bullet_rect.top = int(bullet.pos_y)
                        if enemy_rect.colliderect(bullet_rect):
                            enemies_list.remove(enemy)
                            bullets_list_1.remove(bullet)

                    for bullet in bullets_list_2:
                        bullet_rect = bullet.img.get_rect()
                        bullet_rect.left = int(bullet.pos_x)
                        bullet_rect.top = int(bullet.pos_y)
                        if enemy_rect.colliderect(bullet_rect):
                            enemies_list.remove(enemy)
                            bullets_list_2.remove(bullet)

                time_label.update()
                health_label.update(health_points)
                
                drawer.draw_all(multiplayer)

            elif state == Gv.start_menu:
                if not start_menu.is_active:
                    start_menu.draw()
                    start_menu.is_active = True
                    print("Start")
                if left_click:
                    # start game
                    if Mf.in_seg(start_menu.start_game_button, mouse_pos):
                        multiplayer = False
                        is_beginning = True
                        state = Gv.game
                    # start multiplayer game
                    if Mf.in_seg(start_menu.start_multiplayer_game_button, mouse_pos):
                        multiplayer = True
                        is_beginning = True
                        state = Gv.game
                    # exit
                    if Mf.in_seg(start_menu.quit_game_button, mouse_pos):
                        running = False

            elif state == Gv.lose_menu:
                if not lose_menu.is_active:
                    lose_menu.is_active = True
                    lose_menu.draw()

                if left_click:
                    # restart game
                    if Mf.in_seg(lose_menu.restart_game_button, mouse_pos):
                        state = Gv.game
                        is_beginning = True
                    # exit
                    if Mf.in_seg(lose_menu.quit_game_button, mouse_pos):
                        running = False
                    # return to start menu
                    if Mf.in_seg(lose_menu.home_button, mouse_pos):
                        state = Gv.start_menu

            Gv.fps.tick(60)
            pygame.display.update()

        print('Игра завершена')
        quit()
