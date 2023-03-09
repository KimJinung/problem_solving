SIZE = 5
PERSON = "P"
WALL = "X"
EMPTY_TABLE = "O"


def solution(places):
    answer = []

    for place in places:
        if is_keeping_distance(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer


def is_keeping_distance(waiting_room: list) -> bool:
    for row in range(SIZE):
        for col in range(SIZE):
            if waiting_room[row][col] == PERSON:
                # Diagonal seat
                if row + 1 < SIZE and col + 1 < SIZE:
                    diagonal_seat = waiting_room[row + 1][col + 1]

                    if diagonal_seat == PERSON:
                        if not (
                            waiting_room[row + 1][col] == WALL
                            and waiting_room[row][col + 1] == WALL
                        ):
                            return False

                if row + 1 < SIZE and 0 <= col - 1:
                    diagonal_seat = waiting_room[row + 1][col - 1]

                    if diagonal_seat == PERSON:
                        if not (
                            waiting_room[row + 1][col] == WALL
                            and waiting_room[row][col - 1] == WALL
                        ):
                            return False

                # Down seat
                if row + 1 < SIZE:
                    down_seat = waiting_room[row + 1][col]

                    if down_seat == PERSON:
                        return False

                if row + 2 < SIZE:
                    down_seat = waiting_room[row + 2][col]

                    if down_seat == PERSON:
                        space = waiting_room[row + 1][col]

                        if space != WALL:
                            return False

                # Right seat
                if col + 1 < SIZE:
                    right_seat = waiting_room[row][col + 1]

                    if right_seat == PERSON:
                        return False

                if col + 2 < SIZE:
                    right_seat = waiting_room[row][col + 2]

                    if right_seat == PERSON:
                        space = waiting_room[row][col + 1]

                        if space != WALL:
                            return False

    return True
