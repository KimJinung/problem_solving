def solution(n):
    answer = 0
    
    for num in range(1, n+1):
        if is_case(num):
            answer += 1
        
    return answer

def is_case(num: int) -> bool:
    case = 0
    
    for i in range(1, num+1):
        if num % i == 0:
            case += 1
        
        if case > 2:
            return True
    
    return False
            

"""
약수 개수 구하는 효율적인 방법이 있었던 것으로 기억하는데,
한 번 찾아보기
"""