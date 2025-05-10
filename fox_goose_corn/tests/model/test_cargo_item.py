from fox_goose_corn.src.model.cargo_item import Fox, AbstractCargoItem
from fox_goose_corn.src.model.river import RiverSide


class TestCargoItem:
    def test_cargo_always_starts_the_day_farm_side(self):
        cargo_item: AbstractCargoItem = Fox()

        assert cargo_item.is_at(RiverSide.FARM_SIDE)
        assert not cargo_item.is_at(RiverSide.MARKET_SIDE)

    def test_unload_cargo_item_at(self):
        cargo_item: AbstractCargoItem = Fox()

        cargo_item.unload_cargo_item_at(RiverSide.MARKET_SIDE)

        assert cargo_item.is_at(RiverSide.MARKET_SIDE)
