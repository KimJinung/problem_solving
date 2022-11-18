def solution(dots):
    m = max(dots)
    n = min(dots)
    
    return (m[0] - n[0]) * (m[1] - n[1])
