import math


def solution(k, d):
    answer = 0

    square_d = d**2

    for x_dot in range(0, d + 1, k):
        x_square = x_dot**2
        max_y_square = square_d - x_square

        max_y_dot = int(math.sqrt(max_y_square))

        cnt = max_y_dot // k + 1

        answer += cnt

    return answer


"""
문제에서 언급 하는 선의 길이는 대각선 길이
즉 sqrt(x**2, y**2)가 된다.

최댓값의 square 값에서 x 좌표의 square 값을 빼면 y가 가질 수 있는 최대 square 값이 된다.

해당 값을 square roots 로 계산 하면 해당 값이 y의 최대 좌표다.
그러므로 해당 값에서 interval 만큼 나누고 0을 포함하여 카운팅 한다.
"""
