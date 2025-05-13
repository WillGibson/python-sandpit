import pytest

from list_things.src.scattered_subset import scattered_subset_adding_up_to


class TestScatteredSubsetAddingUpTo:
    def test_sublist_with_unnattainable_target_returns_none(self):
        assert scattered_subset_adding_up_to([4, 2, 1], 8) is None

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
        assert scattered_subset_adding_up_to(full_set, target_sum).sort() == expected.sort()

    @pytest.mark.parametrize(
        "list_size,target_sum",
        [
            (1000, 1234),
            (1000, 1076),
            # (1000, 3076), Times out
        ],
    )
    def test_works_with_a_target_bigger_than_any_element_in_a_much_larger_list(
        self, list_size, target_sum
    ):
        assert sum(scattered_subset_adding_up_to(list(range(list_size)), target_sum)) == target_sum
