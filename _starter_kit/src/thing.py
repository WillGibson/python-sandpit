class Thing:
    _can_act: bool
    _has_acted: bool = False

    def __init__(self, can_act: bool):
        self._can_act = can_act

    def act(self):
        if not self._can_act:
            raise ThingCantActException

        self._has_acted = True

    def has_acted(self) -> bool:
        return self._has_acted


class ThingCantActException(Exception):
    pass
