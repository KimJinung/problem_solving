def solution(s):
    stack = []

    for bracket in s:
        if bracket == "(":
            stack.append(bracket)
        else:
            if len(stack) > 0 and stack[-1] == "(":
                del stack[-1]
            else:
                stack.append(bracket)

    return not stack
