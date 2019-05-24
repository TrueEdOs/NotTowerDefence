from config.Resources import UnitTypes
from controllers.Controller import Controller


class ZombieController(Controller):
    def do(self, unit, all_units):
        target = self.find_nearest_obj(unit, all_units, {UnitTypes.core, UnitTypes.gun})
        if target is None:
            exit(0)
        unit.reload()
        if unit.move(target.pos) is False:
            obj = self.find_nearest_obj(unit, all_units)
            if obj.unit_type is UnitTypes.wall:
                target = obj
        if target:
            unit.attack(target)

