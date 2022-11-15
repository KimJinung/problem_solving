def solution(n):
    return len([num for num in range(1, n+1) if n % num == 0])
            