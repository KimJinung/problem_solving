from functools import cmp_to_key


def solution(numbers):
    nums = map(str, numbers)

    nums = sorted(
        nums, key=cmp_to_key(lambda x, y: 1 if int(x + y) < int(y + x) else -1)
    )

    return str(int("".join(nums)))
