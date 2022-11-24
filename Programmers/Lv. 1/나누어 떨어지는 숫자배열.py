def solution(arr, divisor):
    answer = sorted([num for num in arr if num % divisor == 0])
    return answer if answer else [-1]
