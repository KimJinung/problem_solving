from collections import deque


def solution(prices):
    answer = []

    prices = deque(prices)

    while prices:
        current_price = prices.popleft()

        t = 0

        for price in prices:
            if current_price <= price:
                t += 1
            else:
                t += 1
                break

        answer.append(t)

    return answer
