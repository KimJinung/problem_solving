from collections import defaultdict


def solution(nums):
    N = len(nums)
    phoneketmon = defaultdict(int)

    for num in nums:
        phoneketmon[num] += 1

    answer = len(phoneketmon.keys())

    return answer if answer <= N // 2 else N // 2
