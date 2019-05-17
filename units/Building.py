import Resources
from units.Unit import Unit


class Building(Unit):
    def __init__(self, game_map, controller, hp, pos, width, height, name, unit_type, cost):
        Unit.__init__(self, game_map, controller, hp, pos, width, height, "player", "wall", unit_type)
        self.cost = cost
