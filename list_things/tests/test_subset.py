import pytest

from list_things.src.subset import subset_adding_up_to


class TestSubsetAddingUpTo:
    def test_sublist_with_lots_of_number_and_unnatainable_target_returns_none(self):
        assert subset_adding_up_to([4, 2, 1], 8) is None

    @pytest.mark.parametrize(
        "full_set,target_sum,expected",
        [
            ([1], 1, [1]),
            ([4, 2, 1], 3, [1, 2]),
            ([1, 8, 4, 2, 1], 3, [1, 2]),
            ([1, 8, 4, 2, 1], 4, [4]),
            ([1, 4, 2], 3, [1, 2]),
            ([1, 401, 145, 299, 599, 125, 72, 145], 342, [72, 125, 145]),
            ([1, 4, 8, 2, 1], 15, [1, 2, 4, 8]),
        ],
    )
    def test_returns_subset_adding_up_to_target_sum(self, full_set, target_sum, expected):
        assert subset_adding_up_to(full_set, target_sum) == expected
