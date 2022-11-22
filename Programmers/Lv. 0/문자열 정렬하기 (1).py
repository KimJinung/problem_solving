def solution(my_string):
    answer = [int(item) for item in my_string if item.isdigit()]

    return sorted(answer)
