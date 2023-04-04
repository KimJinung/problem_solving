def solution(n):
    answer = []
    item = 2

    while n != 1:
        if n % item == 0:
            answer.append(item)
            n /= item
        else:
            item += 1

    return sorted(list(set(answer)))
