def solution(numbers, direction):
    if direction == "left":
        return numbers[1:] + numbers[0:1]
    
    return numbers[-1:] + numbers[:-1]