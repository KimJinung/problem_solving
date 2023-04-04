def solution(s):
    length = len(s)
    return True if s.isdigit() and (length == 4 or length == 6) else False
