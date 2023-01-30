from collections import deque


def solution(queue1, queue2):
    sum_of_q1 = sum(queue1)
    sum_of_q2 = sum(queue2)

    total_sum = sum_of_q1 + sum_of_q2

    if total_sum % 2 != 0:
        return -1

    limit = total_sum // 2

    for value in queue1 + queue2:
        if value > limit:
            return -1

    answer = 0

    q1 = deque(queue1)
    q2 = deque(queue2)

    while sum_of_q1 != sum_of_q2:
        if sum_of_q1 > limit:
            item = q1.popleft()
            q2.append(item)

            sum_of_q1 -= item
            sum_of_q2 += item

        elif sum_of_q2 > limit:
            item = q2.popleft()
            q1.append(item)

            sum_of_q2 -= item
            sum_of_q1 += item

        answer += 1

        if answer >= 600000:
            return -1

    return answer
