def solution(array, commands):
    return [get_kth_number(array, command) for command in commands]


def get_kth_number(array, command):
    i, j, k = command

    return sorted(array[i - 1 : j])[k - 1]
