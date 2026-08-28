from typing import Optional

from fox_goose_corn.src.model.boat import Boat
from fox_goose_corn.src.model.cargo_item import (
    AbstractCargoItem,
    CargoEatingCargoException,
)
from fox_goose_corn.src.model.river import RiverSide


class CrossingManager:
    def __init__(
        self,
        boat: Boat,
        pairs_that_cannot_be_left_alone: list[tuple[AbstractCargoItem, AbstractCargoItem]],
    ):
        self._pairs_that_cannot_be_left_alone = pairs_that_cannot_be_left_alone
        self._boat = boat

    def cross_with(self, cargo_item: AbstractCargoItem) -> None:
        self._cargo_left_behind_wont_be_eaten(carried_cargo_item=cargo_item)
        self._boat.add_cargo(cargo_item)
        self._boat.cross_river()

    def cross_empty(self) -> None:
        self._cargo_left_behind_wont_be_eaten(carried_cargo_item=None)
        self._boat.cross_river()

    def _cargo_left_behind_wont_be_eaten(
        self, carried_cargo_item: Optional[AbstractCargoItem]
    ) -> None:
        for one_cargo_item, another_cargo_item in self._pairs_that_cannot_be_left_alone:
            if self._would_be_left_alone_together(
                one_cargo_item, another_cargo_item, carried_cargo_item, self._boat.current_side
            ):
                raise CargoEatingCargoException

    @staticmethod
    def _would_be_left_alone_together(
        one_cargo_item: AbstractCargoItem,
        another_cargo_item: AbstractCargoItem,
        carried_cargo_item: Optional[AbstractCargoItem],
        unattended_side: RiverSide,
    ) -> bool:
        return CrossingManager._would_remain_unattended(
            one_cargo_item, carried_cargo_item, unattended_side
        ) and CrossingManager._would_remain_unattended(
            another_cargo_item, carried_cargo_item, unattended_side
        )

    @staticmethod
    def _would_remain_unattended(
        cargo_item: AbstractCargoItem,
        carried_cargo_item: Optional[AbstractCargoItem],
        unattended_side: RiverSide,
    ) -> bool:
        return cargo_item is not carried_cargo_item and cargo_item.is_at(unattended_side)
