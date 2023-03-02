"""
문제가 요구하는 것
- 2차원 배열에서 가장 큰 정사각형 사이즈를 찾는다

사용할 알고리즘
- DP

아이디어
*처음에 재귀를 사용했고, 효율성 테스트에서 문제가 발생했다.
- 재귀 사용 시 체크한 좌표를 계속해서 중복으로 또다시 확인하는 문제가 있다.
- 그렇다면 반대로 현재 위치에서부터 시작하는 것이 아니라 이전 부분해를 이용해서 현재 위치에서 만들 수 있는 사각형을 확인한다. (DP)

케이스 예시

ex) 대각선, 위, 옆 모두 값이 존재하고 같은 경우
1 1
1 1 이 경우 1,1 좌표는 최대값 + 1인 2가 된다

ex) 대각선, 위, 옆 모두 값이 존재하는데 값이 다른 케이스
1 2
1 2 이 경우 1, 1좌표는 최소값 + 1인 2가 된다.

ex)
0 2
1 1 이 경우 1, 1좌표는 값의 업데이트가 없다.
"""


def solution(board):
    answer = 0

    row_size = len(board)
    col_size = len(board[0])

    for row in range(row_size):
        for col in range(col_size):
            if board[row][col]:
                if 0 <= row - 1 and 0 <= col - 1:
                    diagonal = board[row - 1][col - 1]
                    up = board[row - 1][col]
                    left = board[row][col - 1]

                    if diagonal and up and left:
                        if diagonal == up == left:
                            board[row][col] = up + 1
                        else:
                            board[row][col] = min(diagonal, up, left) + 1

                if board[row][col] > answer:
                    answer = board[row][col]

    return answer * answer
