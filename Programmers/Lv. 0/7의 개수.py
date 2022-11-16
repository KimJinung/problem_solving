def solution(array):
    answer = 0
    
    for num in array:
        str_num = str(num)
        
        answer += str_num.count('7')
        
    return answer