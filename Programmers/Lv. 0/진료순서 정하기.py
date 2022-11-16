def solution(emergency):
    answer = []
    
    sorted_list = sorted(emergency, reverse=True)
    
    for case in emergency:
        value = sorted_list.index(case) + 1
        answer.append(value)
        
    return answer