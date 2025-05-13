import pytest

from list_things.src.continuous_subset import continuous_subset_adding_up_to


class TestContinousSubsetAddingUpTo:
    @pytest.mark.parametrize(
        "full_set,target_sum,expected",
        [
            ([1], 1, [1]),
            ([1, 2, 3, 4], 1, [1]),
            ([1, 2, 3, 4], 3, [1, 2]),
            ([1, 2, 3, 4], 6, [1, 2, 3]),
            ([1, 2, 3, 4], 10, [1, 2, 3, 4]),
            ([1, 2, 3, 4], 9, [2, 3, 4]),
            ([1, 2, 3, 4], 7, [3, 4]),
            ([1, 2, 3, 4], 4, [4]),
        ],
    )
    def test_returns_subset_adding_up_to_target_sum(self, full_set, target_sum, expected):
        assert continuous_subset_adding_up_to(full_set, target_sum) == expected

    def test_sublist_with_unnattainable_target_returns_none(self):
        assert continuous_subset_adding_up_to([13, 2, 1], 8) is None
