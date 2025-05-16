from typing import Optional

from fox_goose_corn.src.model.boat import Boat
from fox_goose_corn.src.model.cargo_item import (
    AbstractCargoItem,
    Fox,
    Goose,
    Corn,
    CargoEatingCargoException,
)


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

    def _check_the_cargo_is_safe(self) -> None:
        if self._fox.is_on_same_side_as(self._goose) or self._goose.is_on_same_side_as(self._corn):
            raise CargoEatingCargoException
