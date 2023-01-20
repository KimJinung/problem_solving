def solution(n):
    remainder_list = []

    while n != 0:
        remainder = n % 3
        n = n // 3

        if remainder == 0:
            remainder = 4
            n -= 1

        remainder_list.append(str(remainder))

    return "".join(remainder_list[::-1])
