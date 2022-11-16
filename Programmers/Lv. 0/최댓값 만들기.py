def solution(numbers):
    numbers.sort()
    
    front = numbers[0] * numbers[1]
    back = numbers[-2] * numbers[-1]
    
    return max(front, back)