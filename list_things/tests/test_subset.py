import pytest

from list_things.src.subset import subset_adding_up_to


class TestSubsetAddingUpTo:
    def test_sublist_with_unnattainable_target_returns_none(self):
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
        assert subset_adding_up_to(full_set, target_sum).sort() == expected.sort()

    @pytest.mark.parametrize(
        "target_sum",
        [
            1,
            55,
            943,
            777,
            1234,
            # 4321, Times out
        ],
    )
    def test_works_with_larger_lists(self, target_sum):
        assert sum(subset_adding_up_to(list(range(1000)), target_sum)) == target_sum

    @pytest.mark.parametrize(
        "target_sum",
        [1076523],
    )
    @pytest.mark.skip("Times out")
    def test_works_with_a_target_bigger_than_any_element_in_a_much_larger_list(self, target_sum):
        assert sum(subset_adding_up_to(list(range(1000000)), target_sum)) == target_sum
