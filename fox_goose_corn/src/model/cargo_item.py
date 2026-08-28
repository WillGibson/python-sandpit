from abc import ABC

from fox_goose_corn.src.model.river import RiverSide


class AbstractCargoItem(ABC):
    def __init__(self) -> None:
        self._current_side: RiverSide = RiverSide.FARM_SIDE

    def is_at(self, expected_side: RiverSide) -> bool:
        return self._current_side is expected_side

    def unload_cargo_item_at(self, side: RiverSide) -> None:
        self._current_side = side


class Fox(AbstractCargoItem):
    pass


class Goose(AbstractCargoItem):
    pass


class Corn(AbstractCargoItem):
    pass


class CargoEatingCargoException(Exception):
    pass
