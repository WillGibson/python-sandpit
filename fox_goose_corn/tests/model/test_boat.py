import pytest
from typeguard import TypeCheckError

from fox_goose_corn.src.model.boat import (
    Boat,
    TooManyCargoItemsException,
    CargoItemNotAtBoatException,
)
from fox_goose_corn.src.model.cargo_item import Fox, Goose, Corn
from fox_goose_corn.src.model.river import RiverSide


class TestBoat:
    def test_boat_always_starts_the_day_farm_side(self):
        boat = Boat()

        assert boat.is_at(RiverSide.FARM_SIDE)
        assert not boat.is_at(RiverSide.MARKET_SIDE)

    def test_each_boat_has_its_own_position(self):
        boat = Boat()
        another_boat = Boat()

        boat.cross_river()

        assert another_boat.is_at(RiverSide.FARM_SIDE)

    def test_boat_can_cross_river_from_farm_to_market(self):
        boat = Boat()

        boat.cross_river()

        assert boat.is_at(RiverSide.MARKET_SIDE)

    def test_boat_can_cross_river_from_market_to_farm(self):
        boat = Boat()
        boat.cross_river()
        assert boat.is_at(RiverSide.MARKET_SIDE)

        boat.cross_river()

        assert boat.is_at(RiverSide.FARM_SIDE)

    def test_boat_can_only_take_expected_cargo_types(self):
        boat = Boat()
        not_a_cargo_item = Boat()

        with pytest.raises(TypeCheckError):
            boat.add_cargo(not_a_cargo_item)

    def test_boat_cannot_take_more_than_one_cargo_item(self):
        boat = Boat()
        cargo_item_1 = Fox()
        cargo_item_2 = Goose()
        boat.add_cargo(cargo_item_1)

        with pytest.raises(TooManyCargoItemsException):
            boat.add_cargo(cargo_item_2)

    def test_boat_cannot_take_cargo_that_is_on_the_opposite_side(self):
        boat = Boat()
        cargo_item = Fox()
        boat.cross_river()

        with pytest.raises(CargoItemNotAtBoatException):
            boat.add_cargo(cargo_item)

    def test_boat_is_still_empty_after_refusing_cargo_from_the_opposite_side(self):
        boat = Boat()
        fox = Fox()
        goose = Goose()
        goose.unload_cargo_item_at(RiverSide.MARKET_SIDE)
        boat.cross_river()
        with pytest.raises(CargoItemNotAtBoatException):
            boat.add_cargo(fox)

        boat.add_cargo(goose)
        boat.cross_river()

        assert goose.is_at(RiverSide.FARM_SIDE)

    @pytest.mark.parametrize("cargo_item_type", [Fox, Goose, Corn])
    def test_boat_can_take_cargo_across_river_from_farm_to_market(self, cargo_item_type):
        boat = Boat()
        cargo_item = cargo_item_type()

        boat.add_cargo(cargo_item)
        boat.cross_river()

        assert cargo_item.is_at(RiverSide.MARKET_SIDE)

    def test_boat_is_empty_after_crossing_with_a_cargo_item(self):
        boat = Boat()
        cargo_item_1 = Fox()
        cargo_item_2 = Goose()
        cargo_item_2.unload_cargo_item_at(RiverSide.MARKET_SIDE)
        boat.add_cargo(cargo_item_1)
        boat.cross_river()

        boat.add_cargo(cargo_item_2)
        boat.cross_river()

        assert cargo_item_2.is_at(RiverSide.FARM_SIDE)
