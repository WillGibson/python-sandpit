import pytest

from list_things.src.continuous_subset import continuous_subset_adding_up_to


class TestContinousSubsetAddingUpTo:
    def test_sublist_with_unnattainable_target_returns_none(self):
        assert continuous_subset_adding_up_to([13, 2, 1], 8) is None

    @pytest.mark.parametrize(
        "full_set,target_sum,expected",
        [
            ([1], 1, [1]),
            ([1, 2, 3, 4], 1, [1]),
            ([1, 2, 3, 4], 3, [3]),
            ([1, 2, 4, 5], 3, [1, 2]),
            ([1, 2, 3, 4], 6, [1, 2, 3]),
            ([1, 2, 3, 4], 10, [1, 2, 3, 4]),
            ([1, 2, 3, 4], 9, [2, 3, 4]),
            ([1, 2, 3, 4], 7, [3, 4]),
            ([1, 2, 3, 4], 4, [4]),
            ([1, 2, 3, 4], 5, [2, 3]),
        ],
    )
    def test_returns_subset_adding_up_to_target_sum(self, full_set, target_sum, expected):
        assert continuous_subset_adding_up_to(full_set, target_sum) == expected

    @pytest.mark.parametrize(
        "list_size,target_sum",
        [
            (1000, 1000),
            (1000, 1076),
            (1000, 13076),
            (10000, 130476),
            (100000, 1500090),
            (1000000, 1),
            (1000000, 500000),
            (1000000, 1000000),
            (1000000, 1500090),
            (10000000, 9790),
            # (10000000, 9700090), # Takes about 2s
            # (10000000, 15000900), # Takes about 3s
            # (10000000, 97000900), # Takes about 30s
        ],
    )
    def test_works_with_larger_lists(self, list_size, target_sum):
        result = continuous_subset_adding_up_to(list(range(list_size + 1)), target_sum)
        print(f"\nResult: {result}")
        assert sum(result) == target_sum
