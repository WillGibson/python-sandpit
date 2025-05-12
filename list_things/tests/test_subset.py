import pytest

from list_things.src.subset import subset_adding_up_to


class TestSubsetAddingUpTo:
    @pytest.mark.parametrize(
        "full_set,target_sum,expected", [([1], 1, [1]), ([4, 2, 1], 3, [2, 1])]
    )
    def test_returns_subset_adding_up_to_target_sum(self, full_set, target_sum, expected):
        assert subset_adding_up_to(full_set, target_sum) == expected

    def test_sublist_with_lots_of_number_and_unnatainable_target_returns_none(self):
        assert subset_adding_up_to([4, 2, 1], 8) is None
