from itertools import combinations
from typing import Optional

from typeguard import typechecked


@typechecked
def scattered_subset_adding_up_to(
    full_set: list[int],
    target_sum: int,
    number_of_elements: int = 1,
) -> Optional[list[int]]:
    for combination in combinations(full_set, number_of_elements):
        if sum(combination) == target_sum:
            return list(combination)

    if number_of_elements < len(full_set):
        # Try again allowing one more element
        return scattered_subset_adding_up_to(full_set, target_sum, number_of_elements + 1)
    else:
        # Not able to find a subset adding up to target
        return None
