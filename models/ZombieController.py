from models.Core import Core


class ZombieController:
    def do(self, unit, all_units):
        core = None
        for is_core in all_units:
            if is_core is Core:
                core = is_core
                break


