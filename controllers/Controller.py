from config.Resources import UnitTypes
from Utils import dist


class Controller:
    def do(self, unit, all_units):
        pass

    def find_nearest_obj(self, unit, units, set_of_types=None):
        found = []

        if set_of_types is None:
            found = units
        else:
            for obj in units:
                if obj.unit_type in set_of_types:
                    found.append(obj)

        if not found: return None
        found = sorted(found, key=lambda obj: dist(unit, obj))
        return found[0] if len(found) == 1 or unit != found[0] else found[1]


