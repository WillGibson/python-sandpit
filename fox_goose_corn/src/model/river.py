from enum import Enum


class RiverSide(Enum):
    FARM_SIDE = "farm-side"
    MARKET_SIDE = "market-side"

    def opposite_side(self) -> "RiverSide":
        return RiverSide.MARKET_SIDE if self is RiverSide.FARM_SIDE else RiverSide.FARM_SIDE
