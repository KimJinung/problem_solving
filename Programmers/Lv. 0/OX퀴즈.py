def solution(quiz):
    answer = ["O" if is_valid(q) else "X" for q in quiz]

    return answer


def is_valid(expression: str) -> bool:
    expression = expression.replace("=", "==")

    return eval(expression)
