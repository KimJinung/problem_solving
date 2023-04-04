def solution(x):
    items = list(map(lambda x: int(x), list(str(x))))

    return True if x % sum(items) == 0 else False
