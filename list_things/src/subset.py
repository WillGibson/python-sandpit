from typing import Optional

# Todo: Look at prefix sums


def subset_adding_up_to(full_set: list[int], target_sum: int) -> Optional[list[int]]:
    full_set.sort(reverse=True)
    output: list[int] = []
    sub_total = 0
    for value in full_set:
        temp_value = sub_total + value
        if temp_value <= target_sum:
            sub_total += value
            output.append(value)
            if temp_value == target_sum:
                output.sort()
                return output

    # Not able to find subset adding uop to target
    return None
