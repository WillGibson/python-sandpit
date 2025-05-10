import pytest

from fox_goose_corn.src.model.boat import (
    Boat,
    CannotCrossToExistingSideException,
    TooManyCargoItemsException,
)
from fox_goose_corn.src.model.cargo_item import Fox, Goose, AbstractCargoItem
from fox_goose_corn.src.model.river import RiverSide


class TestBoat:
    def test_boat_always_starts_the_day_farm_side(self):
        boat: Boat = Boat()

        assert boat.is_at(RiverSide.FARM_SIDE)
        assert not boat.is_at(RiverSide.MARKET_SIDE)

    def test_boat_cannot_cross_from_the_side_its_not_at(self):
        boat: Boat = Boat()

        with pytest.raises(CannotCrossToExistingSideException):
            boat.cross_from(RiverSide.MARKET_SIDE)

    def test_boat_can_cross_river_from_farm_to_market(self):
        boat: Boat = Boat()

        boat.cross_from(RiverSide.FARM_SIDE)

        assert boat.is_at(RiverSide.MARKET_SIDE)

    def test_boat_can_cross_river_from_market_to_farm(self):
        boat: Boat = Boat()
        boat.cross_from(RiverSide.FARM_SIDE)

        boat.cross_from(RiverSide.MARKET_SIDE)

        assert boat.is_at(RiverSide.FARM_SIDE)

    def test_boat_can_take_cargo(self):
        boat: Boat = Boat()
        cargo_item: AbstractCargoItem = Fox()

        boat.add_cargo(cargo_item)

    def test_boat_cannot_take_more_than_one_cargo_item(self):
        boat: Boat = Boat()
        cargo_item_1: AbstractCargoItem = Fox()
        cargo_item_2: AbstractCargoItem = Goose()
        boat.add_cargo(cargo_item_1)

        with pytest.raises(TooManyCargoItemsException):
            boat.add_cargo(cargo_item_2)
