from Globals import GlobalsVar as Gv, GlobalsImg as Gi


# fill screen with background image
def fill_background():
    for x in range(Gv.WIDTH // Gi.Texture_Image.get_width() + 1):
        for y in range(Gv.HEIGHT // Gi.Texture_Image.get_height() + 1):
            Gv.SCREEN.blit(
                Gi.Texture_Image,
                (x * Gi.Texture_Image.get_width(),
                 y * Gi.Texture_Image.get_height())
            )


def generate_base():
    for y in range(Gv.HEIGHT % Gi.Base_Image.get_height() // 2,
                   Gv.HEIGHT - Gi.Base_Image.get_height(),
                   Gi.Base_Image.get_height()):
        Gv.SCREEN.blit(Gi.Base_Image, (5, y))


def in_seg(obj, mouse_pos):
    if mouse_pos['x'] >= obj.pos_x:
        if mouse_pos['x'] <= obj.pos_x + obj.img.get_width():
            if mouse_pos['y'] >= obj.pos_y:
                if mouse_pos['y'] <= obj.pos_y + obj.img.get_height():
                    return True
    return False
