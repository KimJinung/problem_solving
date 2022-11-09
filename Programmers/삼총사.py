from itertools import combinations


def solution(number) -> int:
    number_of_case = list(combinations(number, 3))
            
    trio = [case for case in number_of_case if sum(case) == 0]
    
    return len(trio)
