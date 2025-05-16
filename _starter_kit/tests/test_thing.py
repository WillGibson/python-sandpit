import pytest

from _starter_kit.src.thing import Thing, ThingCantActException


class TestThing:
    def test_new_thing_has_not_acted(self):
        thing = Thing(can_act=True)

        assert not thing.has_acted()

    def test_act_with_true_performs_act(self):
        thing = Thing(can_act=True)

        thing.act()

        assert thing.has_acted()

    def test_act_with_false_raises_thing_cant_act_exception(self):
        thing = Thing(can_act=False)

        with pytest.raises(ThingCantActException):
            thing.act()
