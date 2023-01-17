def solution(dirs):
    answer = 0

    current_dots = [0, 0]

    dots_history_set = set()

    cmd_dict = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

    for cmd in dirs:
        x, y = cmd_dict[cmd]

        dx, dy = current_dots[0] + x, current_dots[1] + y

        if -5 <= dx <= 5 and -5 <= dy <= 5:
            x_history = sorted([current_dots[0], dx])
            y_history = sorted([current_dots[1], dy])

            dots_history_set.add(tuple(x_history + y_history))

            current_dots[0] = dx
            current_dots[1] = dy

    return len(dots_history_set)
