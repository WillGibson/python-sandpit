import pytest

from fox_goose_corn.src.exceptions.cannot_cross_to_existing_side_exception import (
    CannotCrossToExistingSideException,
)
from fox_goose_corn.src.model.boat import Boat
from fox_goose_corn.src.model.river import RiverSide


class TestBoat:
    def test_boat_always_starts_the_day_farm_side(self):
        boat = Boat()

        assert boat.is_at(RiverSide.FARM_SIDE)
        assert not boat.is_at(RiverSide.MARKET_SIDE)

    def test_boat_cannot_cross_from_the_side_its_not_at(self):
        boat = Boat()

        with pytest.raises(CannotCrossToExistingSideException):
            boat.cross(start_from=RiverSide.MARKET_SIDE)

    def test_boat_can_cross_river_from_farm_to_market(self):
        boat = Boat()

        boat.cross(start_from=RiverSide.FARM_SIDE)

        assert boat.is_at(RiverSide.MARKET_SIDE)

    def test_boat_can_cross_river_from_market_to_farm(self):
        boat = Boat()
        boat.cross(start_from=RiverSide.FARM_SIDE)

        boat.cross(start_from=RiverSide.MARKET_SIDE)

        assert boat.is_at(RiverSide.FARM_SIDE)
