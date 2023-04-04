import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville) >= 2 and any(n < K for n in scoville):
        first_food = heapq.heappop(scoville)
        second_food = heapq.heappop(scoville)

        new_food = first_food + (second_food * 2)

        heapq.heappush(scoville, new_food)

        answer += 1

    if all(n >= K for n in scoville):
        return answer

    return -1
