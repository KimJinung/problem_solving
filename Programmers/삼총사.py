from itertools import combinations


def solution(number):
    answer = 0
    
    number_of_case = list(combinations(number, 3))
    
    for case in number_of_case:
        if sum(case) == 0: 
            answer += 1
    
    return answer
