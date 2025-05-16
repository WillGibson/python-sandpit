from itertools import accumulate
from typing import Optional

from typeguard import typechecked


@typechecked
def continuous_subset_adding_up_to(full_set: list[int], target_sum: int) -> Optional[list[int]]:
    full_set.sort()  # Might improve performance on more random lists if the values are in ascending order

    accumulated_sums = list(accumulate(full_set))

    slice_length = 1
    list_length = len(full_set)

    while slice_length <= list_length:
        left_index = 0
        right_index = slice_length - 1
        while right_index < list_length:
            to_subtract = 0 if left_index == 0 else accumulated_sums[left_index - 1]
            if accumulated_sums[right_index] - to_subtract == target_sum:
                return full_set[left_index : left_index + slice_length]
            left_index += 1
            right_index += 1
        slice_length += 1
        # Todo: Might want to add a timeout for things that don't come up in a timely manner

    # Not able to find a subset adding up to target
    return None
