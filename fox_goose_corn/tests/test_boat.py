import pytest

from fox_goose_corn.src.model.boat import Boat
from fox_goose_corn.src.model.river import RiverSide


class TestBoat:
    def test_can_cross_river_in_both_directions(self):
        boat = Boat()

        boat.cross(start_from=RiverSide.MARKET_SIDE)


