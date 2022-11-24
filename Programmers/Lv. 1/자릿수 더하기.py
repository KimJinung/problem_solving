def solution(n):
    str_arr = list(str(n))

    return sum(list(map(lambda x: int(x), str_arr)))
