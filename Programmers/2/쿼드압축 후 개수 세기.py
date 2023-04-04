"""
동일하게 반복되는 패턴 -> 재귀

쿼드압축
1. 2차원 배열이 압축 가능한지 확인한다.
2. 압축 가능하면 업데이트 / 불가능하면 4개의 섹션으로 나누고 재귀에 태운다.
"""

answer = [0, 0]


def solution(arr):
    global answer

    for row in arr:
        for bit in row:
            answer[bit] += 1

    quad_compress(arr)

    return answer


def quad_compress(arr):
    global answer

    size = len(arr)

    if size < 2:
        return

    if result := is_compress(arr):
        bit = arr[0][0]

        answer[bit] -= result - 1
    else:
        size //= 2

        sections = [
            (0, size, 0, size),
            (0, size, size, 2 * size),
            (size, 2 * size, 0, size),
            (size, 2 * size, size, 2 * size),
        ]

        next_sections = []

        for x_st, x_ed, y_st, y_ed in sections:
            section = []
            for x in range(x_st, x_ed):
                row = []
                for y in range(y_st, y_ed):
                    row.append(arr[x][y])

                section.append(row)

            next_sections.append(section)

        for section in next_sections:
            quad_compress(section)


def is_compress(arr: list) -> int:
    prev_bit = arr[0][0]
    cnt = 0

    for row in arr:
        for bit in row:
            if prev_bit != bit:
                return 0

            prev_bit = bit
            cnt += 1

    return cnt
