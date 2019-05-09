from units.Unit import Unit


class MovableUnit(Unit):
    def __init__(self, game, controller, hp, x, y, width, height, speed):
        Unit.__init__(self, game, controller, hp, x, y, width, height)
        self.speed = speed

    def step_to(self, to_x, to_y):
        dx, dy = self.speed
        if to_x < self.x:
            self.x -= dx
        else:
            self.x += dx
        if to_y < self.y:
            self.y -= dy
        else:
            self.y += dy

    def move(self, to_x, to_y):
        self.step_to(to_x, to_y)
        if self.is_blocked():
            self.step_to(-to_x, -to_y)
            return False
        return True

    def is_blocked(self):
        def intersects(obj):
            def is_inside(x, y, obj):
                if obj.x < x < obj.x + obj.width and \
                        obj.y < y < obj.y + obj.height:
                    return True
                return False

            if is_inside(self.x, self.y, obj) or \
                    is_inside(self.x + self.width, self.y, obj) or \
                    is_inside(self.x, self.y + self.height, obj) or \
                    is_inside(self.x + self.width, self.y + self.height, obj):
                return True
            return False

        for unit in self.game.units:
            if intersects(unit):
                return True
