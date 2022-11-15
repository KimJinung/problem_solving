def solution(common):
    case_1 = common[1] - common[0]
    case_2 = common[2] - common[1]
    
    if case_1 == case_2:
        return common[-1] + case_1
    else: 
        return common[-1] * (common[1] / common[0])
        