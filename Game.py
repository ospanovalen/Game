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


class Game:
    @staticmethod
    def start_game():
        # set game name
        pygame.display.set_caption("Tower Defence")

        # define main objects
        player = Player(100, 100)
        time_label = TimeLabel(Gv.FONT, Gv.BLUE, Gv.GREEN, 5, Gv.HEIGHT - 32)
        health_label = HealthLabel(Gv.FONT, Gv.BLUE, Gv.RED, 5, Gv.HEIGHT - 16)

        bullets_list = []
        enemies_list = []
        enemy_delay = 100
        bullets_limit = 2
        speed = 6
        damage = 5
        state = Gv.START_MENU

        keys_dict = {'up': False, 'down': False, 'left': False, 'right': False}
        mouse_pos = {'x': 0, 'y': 0}

        start_menu = StartMenu()
        lose_menu = LoseMenu()

        running = True

        while running:
            # get mouse position
            mouse_pos['x'], mouse_pos['y'] = pygame.mouse.get_pos()
            left_click = False

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    print('Stop')
                    running = False

                # keyboard manager
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        keys_dict['up'] = True
                    elif e.key == pygame.K_DOWN:
                        keys_dict['down'] = True
                    elif e.key == pygame.K_LEFT:
                        keys_dict['left'] = True
                    elif e.key == pygame.K_RIGHT:
                        keys_dict['right'] = True

                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_UP:
                        keys_dict['up'] = False
                    elif e.key == pygame.K_DOWN:
                        keys_dict['down'] = False
                    elif e.key == pygame.K_LEFT:
                        keys_dict['left'] = False
                    elif e.key == pygame.K_RIGHT:
                        keys_dict['right'] = False

                # shoot
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    left_click = True

            if state == Gv.GAME:
                if start_menu.is_active:
                    start_menu.is_active = False
                    health_points = 100
                if lose_menu.is_active:
                    lose_menu.is_active = False
                    health_points = 100

                Mf.fill_background()
                Mf.generate_base()

                # player rotation
                angle_radian = atan2(mouse_pos['y'] - player.pos_y,
                                     mouse_pos['x'] - player.pos_x)
                angle_degree = angle_radian * 180 / pi

                player.rotate(angle_degree)
                player.move(speed, keys_dict)
                if left_click:
                    player.shoot(bullets_list, bullets_limit, angle_radian)

                # bullets movement
                for bullet in bullets_list:
                    bullet.move(speed * 2)
                    bullet.update()

                    if (bullet.pos_x < 0 or bullet.pos_x > Gv.WIDTH or
                            bullet.pos_y < 0 or bullet.pos_y > Gv.HEIGHT):
                        bullets_list.remove(bullet)

                # generate Enemy
                enemy_delay -= randint(0, 3)
                if enemy_delay < 0:
                    pos_y = randint(Gi.Base_Image.get_height(), Gv.HEIGHT - Gi.Base_Image.get_height())
                    enemies_list.append(EnemyFabric.generate(Gv.WIDTH, pos_y, damage))
                    enemy_delay = 100

                # enemy manager
                for enemy in enemies_list:
                    # enemy movement
                    enemy.move(speed)
                    enemy.update()

                    # enemy beat the base
                    if enemy.pos_x < 0 + Gi.Base_Image.get_width() // 2:
                        health_points -= enemy.damage
                        enemies_list.remove(enemy)
                        if health_points <= 0:
                            enemies_list.clear()
                            state = Gv.LOSE_MENU

                    enemy_rect = enemy.img.get_rect()
                    enemy_rect.left = enemy.pos_x
                    enemy_rect.top = enemy.pos_y

                    for bullet in bullets_list:
                        bullet_rect = bullet.img.get_rect()
                        bullet_rect.left = int(bullet.pos_x)
                        bullet_rect.top = int(bullet.pos_y)
                        if enemy_rect.colliderect(bullet_rect):
                            enemies_list.remove(enemy)
                            bullets_list.remove(bullet)

                player.update()
                time_label.update()
                health_label.update(health_points)

            elif state == Gv.START_MENU:
                if not start_menu.is_active:
                    start_menu.draw()
                    start_menu.is_active = True
                    print("Start")
                if left_click:
                    # start game
                    if Mf.in_seg(start_menu.start_game_button, mouse_pos):
                        state = Gv.GAME
                    # exit
                    if Mf.in_seg(start_menu.quit_game_button, mouse_pos):
                        running = False

            elif state == Gv.LOSE_MENU:
                if not lose_menu.is_active:
                    lose_menu.is_active = True
                    lose_menu.draw()

                if left_click:
                    # restart game
                    if Mf.in_seg(lose_menu.restart_game_button, mouse_pos):
                        state = Gv.GAME
                    # exit
                    if Mf.in_seg(lose_menu.quit_game_button, mouse_pos):
                        running = False
                    # return to start menu
                    if Mf.in_seg(lose_menu.home_button, mouse_pos):
                        state = Gv.START_MENU

            Gv.FPS.tick(60)
            pygame.display.update()

        print('Игра завершена')
        quit()
