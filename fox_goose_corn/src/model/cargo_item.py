from abc import abstractmethod, ABC
from typing import Type

from fox_goose_corn.src.model.river import RiverSide


class AbstractCargoItem(ABC):
    _current_side: RiverSide = RiverSide.FARM_SIDE

    def is_at(self, expected_side: RiverSide) -> None:
        return self._current_side is expected_side

    def unload_cargo_item_at(self, side: RiverSide) -> None:
        self._current_side = side

    def is_on_same_side_as(self, other_cargo_item: "AbstractCargoItem") -> bool:
        return self._current_side == other_cargo_item._current_side


class Fox(AbstractCargoItem):
    pass


class Goose(AbstractCargoItem):
    pass


class Corn(AbstractCargoItem):
    pass


class CargoEatingCargoException(Exception):
    pass
