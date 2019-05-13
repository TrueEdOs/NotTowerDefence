from pygame.surface import Surface


def fit_surface(surf, width, height):
    new_surf = Surface((width, height))
    old_width = surf.get_width()
    old_height = surf.get_height()
    for x in range(width):
        for y in range(height):
            new_surf.set_at((x, y), surf.get_at((int(x * (old_width / width)),
                                                 int(y * (old_height / height)))))
    return new_surf


def is_inside(pos, top_left, bottom_right):
    if top_left[0] <= pos[0] <= bottom_right[0] and top_left[1] <= pos[1] <= bottom_right[1]:
        return True
    return False


def is_intersected(x, y):
    if x.pos[0] > y.pos[0] + y.width or x.pos[0] + x.width < y.pos[0] or \
            x.pos[1] > y.pos[1] + y.height or x.pos[1] + x.height < y.pos[1]:
        return False
    return True
