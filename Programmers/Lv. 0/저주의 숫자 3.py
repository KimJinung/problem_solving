def solution(n):
    x3_list = []
    num = 0

    while len(x3_list) <= 100:
        num += 1

        if num % 3 == 0 or "3" in str(num):
            continue

        x3_list.append(num)

    return x3_list[n - 1]
