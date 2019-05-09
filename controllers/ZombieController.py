from units.Core import Core


class ZombieController:
    @staticmethod
    def do(unit, all_units):
        core = None
        for obj in all_units:
            if type(obj) is Core:
                core = obj
                break
        unit.move(core.x, core.y)

