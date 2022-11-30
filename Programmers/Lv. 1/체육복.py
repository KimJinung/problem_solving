def solution(n, lost, reserve):
    filtered_lost = []
    borrow_case1 = []
    borrow_case2 = []

    for student in lost:
        if student in reserve:
            reserve.remove(student)
        else:
            filtered_lost.append(student)

    reserve_for_case1 = reserve[:]
    reserve_for_case2 = reserve[:]

    for student in filtered_lost:
        if student - 1 in reserve_for_case1:
            reserve_for_case1.remove(student - 1)
        elif student + 1 in reserve_for_case1:
            reserve_for_case1.remove(student + 1)
        else:
            borrow_case1.append(student)

        if student + 1 in reserve_for_case2:
            reserve_for_case2.remove(student + 1)
        elif student - 1 in reserve_for_case2:
            reserve_for_case2.remove(student - 1)
        else:
            borrow_case2.append(student)

    return max(n - len(borrow_case1), n - len(borrow_case2))
