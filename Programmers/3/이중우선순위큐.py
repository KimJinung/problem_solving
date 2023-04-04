import heapq


def solution(operations):
    heap = []

    for cmd in operations:
        op, value = cmd.split()

        value = int(value)

        if op == "I":
            heapq.heappush(heap, value)
        elif op == "D" and heap:
            if value == 1:
                heap = swap(heap)
                heapq.heapify(heap)
                heapq.heappop(heap)

                heap = swap(heap)
                heapq.heapify(heap)
            else:
                heapq.heappop(heap)

    if len(heap) < 2:
        return [0, 0]

    min_value = heapq.heappop(heap)

    heap = swap(heap)
    heapq.heapify(heap)

    max_value = -heapq.heappop(heap)

    return [max_value, min_value]


def swap(heap: list) -> list:
    return list(map(lambda x: -x, heap))
