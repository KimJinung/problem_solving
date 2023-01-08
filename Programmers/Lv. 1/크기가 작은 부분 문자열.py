def solution(t, p):
    answer = 0
    
    size = len(p)
    
    for idx in range(0, len(t) - size + 1):
        subset = t[idx: idx + size]
        
        if int(subset) <= int(p):
            answer += 1
    
    return answer