def solution(my_string):
    integer = "".join(i if i.isdigit() else " " for i in my_string)
    return sum(int(i) for i in integer.split())
