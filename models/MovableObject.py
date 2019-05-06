from models.GameObject import GameObject


class MovableObject(GameObject):
    def __init__(self, game, controller, hp, x, y, width, height, speed):
        GameObject.__init__(self, game, controller, hp, x, y, width, height)
        self.speed = speed

    def move(self, to_x, to_y):
        if (self.x - to_x)**2 + (self.y - to_y)**2 > self.speed**2:
            return False
        return True
