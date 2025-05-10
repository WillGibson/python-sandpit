from fox_goose_corn.src.model.river import RiverSide


class AbstractCargoItem:
    _current_side: RiverSide = RiverSide.FARM_SIDE

    def is_at(self, expected_side: RiverSide):
        return self._current_side is expected_side

    def unload_cargo_item_at(self, side: RiverSide):
        self._current_side = side


class Fox(AbstractCargoItem):
    pass


class Goose(AbstractCargoItem):
    pass


class Corn(AbstractCargoItem):
    pass
