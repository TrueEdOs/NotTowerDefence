from units.Core import Core
from config.Resources import UnitTypes
from controllers.Controller import Controller


class CannonController(Controller):
    def do(self, unit, all_units):
        target = self.find_nearest_obj(unit, all_units, {UnitTypes.enemy})
        unit.reload()
        if target:
            unit.attack(target)
