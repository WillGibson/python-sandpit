from typing import Optional

# Todo: Look at prefix sums


def subset_adding_up_to(full_set: list[int], target_sum: int) -> Optional[list[int]]:
    output: list[int] = []
    sub_total = 0
    for value in full_set:
        temp_value = sub_total + value
        if temp_value <= target_sum:
            sub_total += value
            output.append(value)
            if temp_value == target_sum:
                break

    if sub_total == target_sum:
        return output
    else:
        return None
