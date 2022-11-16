def solution(array, n):
    array.sort()
    
    min_value = n
    answer = None
    
    for num in array:
        value = abs(n - num)
        
        if value < min_value:
            min_value = value
            answer = num
            
    return answer