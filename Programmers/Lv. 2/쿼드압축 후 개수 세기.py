# 섹션 나누는 코드를 만들지 못했음
# 섹션을 구하면 굳이 플래그 비트까지 사용할 필요가 없을듯?
def solution(arr):
    answer = [0, 0]

    # 1. 초기값 설정
    size = len(arr)

    for subset in arr:
        for bit in subset:
            answer[bit] += 1

    # 2. 압축
    n = size // 2

    while n != 1:
        sections = [
            (0, n, 0, n),
            (0, n, n, 2 * n),
            (n, 2 * n, 0, n),
            (n, 2 * n, n, 2 * n),
        ]

        for x_start, x_end, y_start, y_end in sections:
            quad = arr[x_start][y_start]

            if quad != -1:
                if result := is_compress(x_start, x_end, y_start, y_end, arr):
                    answer[quad] -= result - 1

                    arr = set_complete(x_start, x_end, y_start, y_end, arr)

        n //= 2

    return answer


def is_compress(x_start, x_end, y_start, y_end, arr) -> int:
    prev = arr[x_start][y_start]

    cnt = 0

    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            if prev != arr[x][y]:
                return 0

            prev = arr[x][y]

            cnt += 1

    return cnt


def set_complete(x_start, x_end, y_start, y_end, arr) -> list:
    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            arr[x][y] = -1

    return arr
