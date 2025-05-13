from itertools import accumulate
from typing import Optional


def continuous_subset_adding_up_to(full_set: list[int], target_sum: int) -> Optional[list[int]]:
    accumulated_sums = list(accumulate(full_set))

    slice_length = 1
    list_length = len(full_set)
    while slice_length <= list_length:
        left_index = 0
        while left_index <= list_length - slice_length:
            right_index = left_index + slice_length - 1
            if left_index == 0:
                if accumulated_sums[right_index] == target_sum:
                    return full_set[left_index:slice_length]
            elif accumulated_sums[right_index] - accumulated_sums[left_index - 1] == target_sum:
                if slice_length == 1:
                    return [full_set[right_index]]
                else:
                    return full_set[left_index : left_index + slice_length]
            left_index += 1
        slice_length += 1

    # Not able to find a subset adding up to target
    return None
