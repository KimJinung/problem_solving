def solution(number, k):
    stack = []

    for num in number:
        while stack and k > 0:
            if num > stack[-1]:
                stack.pop()
                k -= 1
            else:
                break

        stack.append(num)

    if k != 0:
        stack = stack[:-k]

    return "".join(stack)


"""
처음 접근 방법
1. 삭제할 인덱스 전부 구한다.
2. 위 인덱스만 남기고 이어 붙인다.

더 나은 방법
1. stack을 이용해서 현재 숫자보다 이전에 나온 숫자가 작은 경우 모두 제거한다. 
"""
