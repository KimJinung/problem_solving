def solution(date1, date2):
    for idx in range(3):
        if date1[idx] < date2[idx]:
            return 1
        elif date1[idx] > date2[idx]:
            return 0

    return 0
