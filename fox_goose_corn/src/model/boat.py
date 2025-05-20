from typing import Optional

from typeguard import typechecked

from fox_goose_corn.src.model.cargo_item import AbstractCargoItem
from fox_goose_corn.src.model.river import RiverSide


@typechecked
class Boat:
    _current_side: RiverSide = RiverSide.FARM_SIDE
    _cargo_item: Optional[AbstractCargoItem] = None

    def cross_river(self):
        self._current_side = (
            RiverSide.MARKET_SIDE
            if self._current_side is RiverSide.FARM_SIDE
            else RiverSide.FARM_SIDE
        )

        if self._cargo_item is not None:
            self._unload_cargo_item()

    def is_at(self, expected_side: RiverSide):
        return self._current_side is expected_side

    def add_cargo(self, cargo_item: AbstractCargoItem):
        if not isinstance(cargo_item, AbstractCargoItem):
            raise InvalidCargoItemException

        if self._cargo_item is not None:
            raise TooManyCargoItemsException

        self._cargo_item = cargo_item

    def _unload_cargo_item(self):
        self._cargo_item.unload_cargo_item_at(self._current_side)
        self._cargo_item = None


class InvalidCargoItemException(Exception):
    pass


class TooManyCargoItemsException(Exception):
    pass
