"""
문제가 요구하는 것
- 최단 경로의 개수

사용할 알고리즘
- DP

아이디어
- 특정 좌표까지 도달할 수 있는 최단 거리의 개수는, (row, col-1), (row-1, col) 좌표까지 도달 할 수 있는 경우의 수의 합
"""

def solution(m, n, puddles):
    road = [[0 for _ in range(m)] for _ in range(n)]
    
    for col, row in puddles:
        road[row - 1][col - 1] = "#"
    
    road[0][0] = 1
    
    for row in range(n):
        for col in range(m):
            if road[row][col] != "#":
                if 0 <= row - 1:
                    up = road[row - 1][col]
                    
                    if up != "#":
                        road[row][col] += up
                
                if 0 <= col - 1:
                    left = road[row][col - 1]
                    
                    if left != "#":
                        road[row][col] += left
                    
                
    return road[n - 1][m - 1] % 1000000007
