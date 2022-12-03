def solution(s):
    stack = []

    for ch in s:
        if len(stack) > 0 and stack[-1] == ch:
            del stack[-1]
        else:
            stack.append(ch)

    return 0 if stack else 1
