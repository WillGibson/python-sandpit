from fox_goose_corn.src.model.cargo_item import Fox
from fox_goose_corn.src.model.river import RiverSide


class TestCargoItem:
    def test_cargo_always_starts_the_day_farm_side(self):
        cargo_item = Fox()

        assert cargo_item.is_at(RiverSide.FARM_SIDE)
        assert not cargo_item.is_at(RiverSide.MARKET_SIDE)

    def test_unload_cargo_item_at(self):
        cargo_item = Fox()

        cargo_item.unload_cargo_item_at(RiverSide.MARKET_SIDE)

        assert cargo_item.is_at(RiverSide.MARKET_SIDE)

    def test_is_on_same_side_as_with_items_on_same_side_returns_true(self):
        cargo_item_1 = Fox()
        cargo_item_2 = Fox()

        assert cargo_item_1.is_on_same_side_as(cargo_item_2)

    def test_is_on_same_side_as_with_items_on_different_sides_returns_false(self):
        cargo_item_1 = Fox()
        cargo_item_2 = Fox()
        cargo_item_2.unload_cargo_item_at(RiverSide.MARKET_SIDE)

        assert not cargo_item_1.is_on_same_side_as(cargo_item_2)
