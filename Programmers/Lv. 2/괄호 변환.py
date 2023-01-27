def solution(p):
    return recursive(p)


def recursive(w: str) -> str:
    if not w:
        return ""

    u, v = split(w)

    if is_correct(u):
        return u + recursive(v)

    return "(" + recursive(v) + ")" + reverse_bracket(u[1:-1])


def split(w: str) -> (str, str):
    u = ""

    op_bracket, cl_bracket = 0, 0

    for idx, bracket in enumerate(w):
        u += bracket

        if bracket == "(":
            op_bracket += 1
        else:
            cl_bracket += 1

        if op_bracket == cl_bracket:
            return u, w[idx + 1 :]


def is_correct(w: str) -> bool:
    stack = []

    for bracket in w:
        if stack and stack[-1] == "(" and bracket == ")":
            stack.pop()
            continue

        stack.append(bracket)

    return not stack


def reverse_bracket(w: str) -> str:
    reverse = {"(": ")", ")": "("}

    return "".join(reverse[br] for br in w)
