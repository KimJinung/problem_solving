"""
문제가 요구하는 것
- 필요로 하는 인자를 모두 가진 배열의 최소 범위 


사용할 자료구조
- deque


아이디어
1. 큐가 조건을 만족할 때까지 인자를 삽입한다.
2. 조건을 만족하는 경우 조건을 만족하지 않을 때까지 popleft를 반복한다.
3. 조건을 만족하지 않기 시작할 때의 head - 1, tail이 정답이 될 수 있는 케이스다.
4. 다시 1번부터 반복한다.

*조건을 만족하는 케이스 검사를 어떻게 최적화 할 것인가?
- 이전까지 찾은 답의 길이보다 큰 케이스는 검사하지 않는다.
- hash 이용해서 각 보석의 uid를 생성한다 + 배열에 개수를 저장하고 있는다.
"""


from collections import deque


def solution(gems):
    answer = []

    juwerly_set = set(gems)
    juwerly_size = len(juwerly_set)
    juwerly_dict = {item: idx for idx, item in enumerate(juwerly_set)}
    juwerly_collection = [0 for _ in range(juwerly_size)]

    Q = deque([])

    head, tail = 0, 0
    max_size = len(gems) + 1

    while tail < len(gems):
        # Update juwelry collection
        juwel = gems[tail]

        Q.append(juwel)

        item_uid = juwerly_dict[juwel]

        juwerly_collection[item_uid] += 1

        # Exclude case when size greather than current max size
        if tail - head + 1 >= max_size:
            while Q and tail - head + 1 >= max_size:
                juwel = Q.popleft()

                item_uid = juwerly_dict[juwel]

                juwerly_collection[item_uid] -= 1

                head += 1

        # If array meet condition
        if all(juwerly_collection):
            cnt = 0

            while all(juwerly_collection):
                juwel = Q.popleft()

                item_uid = juwerly_dict[juwel]

                juwerly_collection[item_uid] -= 1

                cnt += 1

            head += cnt

            answer = [head, tail + 1]

            if answer[1] - answer[0] + 1 < max_size:
                max_size = answer[1] - answer[0] + 1

        tail += 1

    return answer
