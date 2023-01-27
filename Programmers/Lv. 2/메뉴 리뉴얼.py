from itertools import combinations
from collections import defaultdict, Counter


def solution(orders, course):
    answer = []

    # 1. Make history of menu combinations
    order_history = defaultdict(int)

    for order in orders:
        for case in course:
            for menu in combinations(order, case):
                menu = "".join(sorted(menu))
                order_history[menu] += 1

    # 2. Find max count combination by course
    max_order_by_course = defaultdict(int)

    for order, count in order_history.items():
        if count >= 2:
            course = len(order)

            if max_order_by_course[course] < count:
                max_order_by_course[course] = count

    # 3. Check menu by max order history
    for order, count in order_history.items():
        course = len(order)

        if max_order_by_course[course] == count:
            answer.append(order)

    return sorted(answer)


"""
Counter 함수, Most common 메서드를 이용한 풀이
"""

from itertools import combinations
from collections import defaultdict, Counter


def solution2(orders, course):
    answer = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)

        max_orders = Counter(order_combinations).most_common()

        answer += [
            key for key, value in max_orders if value > 1 and value == max_orders[0][1]
        ]

    return ["".join(menu) for menu in sorted(answer)]
