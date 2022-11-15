def solution(my_string):
    return sum([int(item) for item in my_string if item.isdigit()])