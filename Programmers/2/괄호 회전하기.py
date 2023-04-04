def solution(s):
    answer = 0

    for _ in range(len(s)):
        if is_valid(s):
            answer += 1

        s = s[1:] + s[0]

    return answer


def is_valid(s: str) -> bool:
    stack = []

    for bracket in s:
        if bracket in ["(", "[", "{"]:
            stack.append(bracket)
        else:
            if len(stack) > 0:
                op_bracket = stack[-1]

                if op_bracket != "(" and bracket == ")":
                    stack.append(bracket)
                elif op_bracket != "[" and bracket == "]":
                    stack.append(bracket)
                elif op_bracket != "{" and bracket == "}":
                    stack.append(bracket)
                else:
                    del stack[-1]

            else:
                return False

    return len(stack) == 0
