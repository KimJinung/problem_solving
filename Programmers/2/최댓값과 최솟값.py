def solution(s):
    result = [int(num) for num in s.split()]

    return f"{min(result)} {max(result)}"
