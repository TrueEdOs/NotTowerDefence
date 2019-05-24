import Utils
from config.Resources import UnitTypes
from controllers.Controller import Controller


class ZombieController(Controller):
    def __init__(self):
        self.good_points = []

    def do(self, unit, all_units):
        target = list(all_units)[0]
        #target = self.find_nearest_obj(unit, all_units, {UnitTypes.core})
        better_target = target.pos
        priority = unit.hp - 6
        for point in self.good_points:
            if Utils.classical_dist(better_target, target.pos) > Utils.classical_dist(point[0], target.pos) \
                    or (Utils.classical_dist(better_target, target.pos) > Utils.classical_dist(point[0], target.pos) - 40 and point[1] > priority):
                better_target = point[0]
                priority = point[1]

        if target is None:
            exit(0)

        unit.reload()
        if unit.move(better_target) is False:
            obj = self.find_nearest_obj(unit, all_units)
            if obj.unit_type is UnitTypes.wall:
                target = obj
        if target:
            unit.attack(target)

        self.good_points.append((unit.pos, unit.hp))

        if len(self.good_points) > 1000:
            self.good_points.clear()
