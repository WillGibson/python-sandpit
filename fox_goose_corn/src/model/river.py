from enum import Enum

from typeguard import typechecked


@typechecked
class RiverSide(Enum):
    FARM_SIDE: str = "farm-side"
    MARKET_SIDE: str = "market-side"
