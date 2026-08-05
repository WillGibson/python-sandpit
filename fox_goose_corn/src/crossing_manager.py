from typeguard import typechecked

from fox_goose_corn.src.model.boat import Boat
from fox_goose_corn.src.model.cargo_item import (
    AbstractCargoItem,
    Fox,
    Goose,
    Corn,
    CargoEatingCargoException,
)
from fox_goose_corn.src.model.river import RiverSide


@typechecked
class CrossingManager:
    def __init__(self, boat: Boat, fox: Fox, goose: Goose, corn: Corn):
        self._corn = corn
        self._goose = goose
        self._fox = fox
        self._boat = boat

    def cross_with(self, cargo_item: AbstractCargoItem) -> None:
        self._boat.add_cargo(cargo_item)
        self._boat.cross_river()
        self._check_the_cargo_is_safe()

    def cross_empty(self) -> None:
        self._boat.cross_river()
        self._check_the_cargo_is_safe()

    def _check_the_cargo_is_safe(self) -> None:
        unattended_side = self._side_the_boat_is_not_at()

        if self._are_left_alone_together(
            self._fox, self._goose, unattended_side
        ) or self._are_left_alone_together(self._goose, self._corn, unattended_side):
            raise CargoEatingCargoException

    def _side_the_boat_is_not_at(self) -> RiverSide:
        return (
            RiverSide.MARKET_SIDE if self._boat.is_at(RiverSide.FARM_SIDE) else RiverSide.FARM_SIDE
        )

    @staticmethod
    def _are_left_alone_together(
        one_cargo_item: AbstractCargoItem,
        another_cargo_item: AbstractCargoItem,
        unattended_side: RiverSide,
    ) -> bool:
        return one_cargo_item.is_at(unattended_side) and another_cargo_item.is_at(unattended_side)
