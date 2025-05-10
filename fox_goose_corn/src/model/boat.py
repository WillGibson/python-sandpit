from fox_goose_corn.src.exceptions.cannot_cross_to_existing_side_exception import (
    CannotCrossToExistingSideException,
)
from fox_goose_corn.src.model.river import RiverSide


class Boat:
    current_side: RiverSide = RiverSide.FARM_SIDE

    def cross(self, start_from: RiverSide):
        if start_from != self.current_side:
            raise CannotCrossToExistingSideException

        self.current_side = (
            RiverSide.MARKET_SIDE if start_from is RiverSide.FARM_SIDE else RiverSide.FARM_SIDE
        )

    def is_at(self, expected_side: RiverSide):
        return self.current_side is expected_side
