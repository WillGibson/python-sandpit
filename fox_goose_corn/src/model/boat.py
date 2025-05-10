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
        if self._cargo_item is not None:
            raise TooManyCargoItemsException

        self._cargo_item = cargo_item

    def test_boat_can_take_cargo_across_river_from_farm_to_market(self):
        boat: Boat = Boat()
        cargo_item: AbstractCargoItem = Fox()

        boat.add_cargo(cargo_item)
        boat.cross_from(RiverSide.FARM_SIDE)

        assert cargo_item.is_at(RiverSide.MARKET_SIDE)


class CannotCrossToExistingSideException(Exception):
    pass


class TooManyCargoItemsException(Exception):
    pass
