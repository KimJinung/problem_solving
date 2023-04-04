def solution(num, total):
    center = total // num
    left_sub_count = 0
    right_sub_count = 0

    if total % num > 0:
        left_sub_count = num // 2 - 1
        right_sub_count = num // 2

    else:
        left_sub_count = num // 2
        right_sub_count = num // 2

    left = [x for x in range(center - left_sub_count, center)]
    right = [x for x in range(center + 1, center + right_sub_count + 1)]

    return left + [center] + right
