def solution(board, moves):
    answer = 0

    basket = []

    for line in moves:
        doll, board = pull(line - 1, board)

        if doll == 0:
            continue

        if len(basket) > 0 and basket[-1] == doll:
            answer += 2

            basket.pop()
        else:
            basket.append(doll)

    return answer


def pull(line: int, board: list) -> tuple([int, list]):
    length_of_line = len(board)

    for idx in range(length_of_line):
        doll = board[idx][line]

        if doll != 0:
            board[idx][line] = 0

            return doll, board

    return 0, board
