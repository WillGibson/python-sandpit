from itertools import combinations, accumulate
from typing import Optional


def continuous_subset_adding_up_to(full_set: list[int], target_sum: int) -> Optional[list[int]]:
    accumulated_sums = list(accumulate(full_set))

    start_index = 0
    while len(full_set) > 0:
        maximum_end_index = len(accumulated_sums) - 1
        end_index = start_index
        while end_index <= maximum_end_index:
            if accumulated_sums[end_index] == target_sum:
                return full_set[start_index : end_index + 1]
            elif accumulated_sums[end_index] - accumulated_sums[start_index] == target_sum:
                return full_set[start_index + 1 : end_index + 1]
            end_index += 1

        # Move in one from the left
        del full_set[0]
        del accumulated_sums[0]

    # Not able to find a subset adding up to target
    return None
