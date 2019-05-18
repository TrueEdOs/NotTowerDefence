from units.Core import Core
from config.Resources import UnitTypes


class ZombieController:
    def do(self, unit, all_units):
        core = None
        for obj in all_units:
            if UnitTypes.core == obj.unit_type:
                core = obj
                break
        unit.move(core.pos)
        #unit.attack(core)
        #print(unit.pos)

