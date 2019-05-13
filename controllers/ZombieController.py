import Resources
from units.Core import Core


class ZombieController:
    def do(self, unit, all_units):
        core = None
        for obj in all_units:
            if Resources.UnitTypes.core == obj.unit_type:
                core = obj
                break
        unit.move(core.pos)

