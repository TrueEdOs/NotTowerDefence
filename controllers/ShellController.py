from controllers.Controller import Controller


class ShellController(Controller):
    def do(self, unit, all_units):
        unit.move(unit.target_direction)
        target = self.find_nearest_obj(unit, all_units)
        unit.reload()
        if target:
            unit.attack(target)
