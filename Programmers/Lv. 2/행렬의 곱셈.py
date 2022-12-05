def solution(arr1, arr2):
    return [
        [sum(x * y for x, y in zip(row, col)) for col in zip(*arr2)] for row in arr1
    ]
