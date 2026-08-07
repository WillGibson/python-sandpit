import pytest

from fox_goose_corn.src.model.river import RiverSide


class TestRiverSide:
    @pytest.mark.parametrize(
        "side, expected_opposite",
        [
            (RiverSide.FARM_SIDE, RiverSide.MARKET_SIDE),
            (RiverSide.MARKET_SIDE, RiverSide.FARM_SIDE),
        ],
    )
    def test_a_river_side_knows_its_opposite_side(self, side, expected_opposite):
        assert side.opposite_side() is expected_opposite
