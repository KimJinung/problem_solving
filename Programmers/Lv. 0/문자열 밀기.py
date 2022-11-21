def solution(A, B):
    answer = 0
    
    current_string = A
    
    if current_string == B:
        return 0
    
    for i in range(len(A)):
        current_string = current_string[-1] + current_string[:-1]
        
        if current_string == B:
            return i+1
    
    return -1