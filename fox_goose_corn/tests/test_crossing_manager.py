import pytest

from fox_goose_corn.src.crossing_manager import CrossingManager
from fox_goose_corn.src.model.boat import (
    Boat,
)
from fox_goose_corn.src.model.cargo_item import Corn, Fox, Goose, CargoEatingCargoException
from fox_goose_corn.src.model.river import RiverSide


class TestCrossingManager:
    # Farm side
    def test_fox_cannot_be_left_farm_side_with_goose(self):
        crossing, fox, goose, corn = self._setup()

        with pytest.raises(CargoEatingCargoException):
            crossing.cross_with(corn)

    def test_goose_cannot_be_left_farm_side_with_corn(self):
        crossing, fox, goose, corn = self._setup()

        with pytest.raises(CargoEatingCargoException):
            crossing.cross_with(fox)

    def test_corn_can_be_left_farm_side_with_fox(self):
        crossing, fox, goose, corn = self._setup()

        crossing.cross_with(goose)

    # Market side
    def test_fox_cannot_be_left_market_side_with_goose(self):
        crossing, fox, goose, corn = self._setup()
        crossing.cross_with(goose)
        crossing.cross_empty()
        crossing.cross_with(fox)

        with pytest.raises(CargoEatingCargoException):
            crossing.cross_empty()

    def test_goose_cannot_be_left_market_side_with_corn(self):
        crossing, fox, goose, corn = self._setup()
        crossing.cross_with(goose)
        crossing.cross_empty()
        crossing.cross_with(corn)

        with pytest.raises(CargoEatingCargoException):
            crossing.cross_empty()

    def test_corn_can_be_left_market_side_with_fox(self):
        crossing, fox, goose, corn = self._setup()
        crossing.cross_with(goose)
        crossing.cross_empty()
        crossing.cross_with(corn)
        crossing.cross_with(goose)

        crossing.cross_with(fox)

    # The whole journey
    def test_all_cargo_items_can_be_taken_to_market(self):
        crossing, fox, goose, corn = self._setup()

        crossing.cross_with(goose)
        crossing.cross_empty()
        crossing.cross_with(corn)
        crossing.cross_with(goose)
        crossing.cross_with(fox)
        crossing.cross_empty()
        crossing.cross_with(goose)

        assert fox.is_at(RiverSide.MARKET_SIDE)
        assert goose.is_at(RiverSide.MARKET_SIDE)
        assert corn.is_at(RiverSide.MARKET_SIDE)

    @staticmethod
    def _setup():
        boat = Boat()
        fox = Fox()
        goose = Goose()
        corn = Corn()
        crossing = CrossingManager(boat, fox, goose, corn)
        return crossing, fox, goose, corn
