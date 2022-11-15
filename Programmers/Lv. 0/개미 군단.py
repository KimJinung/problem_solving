def solution(hp):
    answer = 0
    
    for ant in [5, 3, 1]:
        cnt = hp // ant
        hp -= ant * cnt
        
        answer += cnt
            
    return answer