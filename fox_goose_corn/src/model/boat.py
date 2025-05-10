from fox_goose_corn.src.model.cargo_item import AbstractCargoItem, Fox
from fox_goose_corn.src.model.river import RiverSide


class Boat:
    _current_side: RiverSide = RiverSide.FARM_SIDE
    _cargo_item: AbstractCargoItem = None

    def cross_from(self, start_from: RiverSide):
        if start_from != self._current_side:
            raise CannotCrossToExistingSideException

        self._current_side = (
            RiverSide.MARKET_SIDE if start_from is RiverSide.FARM_SIDE else RiverSide.FARM_SIDE
        )

        if self._cargo_item is not None:
            self._cargo_item.unload_cargo_item_at(self._current_side)

    def is_at(self, expected_side: RiverSide):
        return self._current_side is expected_side

    def add_cargo(self, cargo_item: AbstractCargoItem):
        if not isinstance(cargo_item, AbstractCargoItem):
            raise InvalidCargoItemException

        if self._cargo_item is not None:
            raise TooManyCargoItemsException

        self._cargo_item = cargo_item


class CannotCrossToExistingSideException(Exception):
    pass


class InvalidCargoItemException(Exception):
    pass


class TooManyCargoItemsException(Exception):
    pass
