import pytest

from fox_goose_corn.src.crossing_manager import CrossingManager
from fox_goose_corn.src.model.boat import (
    Boat,
)
from fox_goose_corn.src.model.cargo_item import Corn, Fox, Goose, CargoEatingCargoException


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

        with pytest.raises(CargoEatingCargoException):
            crossing.cross_with(fox)

    def test_goose_cannot_be_left_market_side_with_corn(self):
        crossing, fox, goose, corn = self._setup()
        crossing.cross_with(goose)
        crossing.cross_empty()

        with pytest.raises(CargoEatingCargoException):
            crossing.cross_with(corn)

    @pytest.mark.skip
    # Todo: Need to deal with wthere the farmer is still there to supervise the items or not
    def test_corn_can_be_left_market_side_with_fox(self):
        crossing, fox, goose, corn = self._setup()
        crossing.cross_with(goose)
        crossing.cross_empty()
        crossing.cross_with(corn)
        crossing.cross_with(goose)

        crossing.cross_with(fox)

    @staticmethod
    def _setup():
        boat = Boat()
        fox = Fox()
        goose = Goose()
        corn = Corn()
        crossing = CrossingManager(boat, fox, goose, corn)
        return crossing, fox, goose, corn
