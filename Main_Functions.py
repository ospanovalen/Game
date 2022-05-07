from Globals import GlobalsVar as Gv, GlobalsImg as Gi


# fill screen with background image
def fill_background():
    for x in range(Gv.width // Gi.texture_image.get_width() + 1):
        for y in range(Gv.height // Gi.texture_image.get_height() + 1):
            Gv.screen.blit(
                Gi.texture_image,
                (x * Gi.texture_image.get_width(),
                 y * Gi.texture_image.get_height())
            )


def generate_base():
    for y in range(Gv.height % Gi.base_image.get_height() // 2,
                   Gv.height - Gi.base_image.get_height(),
                   Gi.base_image.get_height()):
        Gv.screen.blit(Gi.base_image, (5, y))


def in_seg(obj, mouse_pos):
    if mouse_pos['x'] >= obj.pos_x:
        if mouse_pos['x'] <= obj.pos_x + obj.img.get_width():
            if mouse_pos['y'] >= obj.pos_y:
                if mouse_pos['y'] <= obj.pos_y + obj.img.get_height():
                    return True
    return False


def get_angle(keys_dict: dict) -> float:
    if keys_dict['up']:
        if keys_dict['right']:
            angle = 45
        elif keys_dict['left']:
            angle = 135
        else:
            angle = 90
    elif keys_dict['down']:
        if keys_dict['right']:
            angle = -45
        elif keys_dict['left']:
            angle = -135
        else:
            angle = -90
    elif keys_dict['left']:
        angle = 180
    else:
        angle = 0
    return angle
