"""
수식을 직접 계산하는 비지니스 로직에서 어려움을 겪었던 문제임

1. 스택 두 개를 두고,
2. 계산해서 한 쪽 스택에 몰아두고,
3. 다시 스택을 스왑해서 계산을 이어나가는 방법을 활용
"""
from itertools import permutations
from collections import deque
import re


def solution(expression):
    answer = []

    # 1. Make number of cases using operators
    operators = set(op for op in expression if op in ("*", "+", "-"))

    cases = permutations(operators, len(operators))

    # 2. Calculate by cases
    expression = re.findall(r"\d+|[\*\+\-]", expression)

    for case in cases:
        stack1 = expression
        stack2 = []

        op_queue = deque(case)

        while op_queue:
            op = op_queue.popleft()

            trigger = ""

            for item in stack1:
                if item == op:
                    trigger = op
                elif trigger:
                    # result = eval(stack2.pop() + trigger + item)
                    result = calcul(trigger, stack2.pop(), item)
                    stack2.append(result)
                    trigger = ""
                else:
                    stack2.append(item)

            stack1, stack2 = stack2, []

        answer.append(abs(int(stack1[0])))

    return max(answer)


def calcul(op: str, value1: str, value2: str) -> str:
    value1 = int(value1)
    value2 = int(value2)

    if op == "*":
        return str(value1 * value2)
    elif op == "+":
        return str(value1 + value2)
    else:
        return str(value1 - value2)
