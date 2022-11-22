from collections import defaultdict


def solution(array):
    answer = 0

    num_dict = defaultdict(int)

    for num in array:
        num_dict[num] += 1

    max_count = max(num_dict.values())

    for key, value in num_dict.items():
        if value == max_count:
            if answer != 0:
                return -1

            answer = key

    return answer
