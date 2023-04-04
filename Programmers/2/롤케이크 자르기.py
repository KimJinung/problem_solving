"""
문제에서 요구하는 것
- 배열을 이등분 했을 때 양측 배열이 가지는 고유 인자 개수가 같은 경우는 몇개인가?

사용할 자료구조
- 큐
- 해시

아이디어
- 좌, 우측 배열이 가지고 있는 고유한 인자의 개수가 같아지는 케이스를 찾는다.
1. 좌측은 set을 사용한다.
2. 우측은 큐와 해시를 이용해서 팝하는 인자의 개수를 카운팅한다. 0이 되면 키에서 제거한다.
* 이때 해시를 써서 시간 복잡도와 공간 복잡도를 트레이드한다.
"""


from collections import deque, Counter


def solution(topping):
    answer = 0

    left_cake = set()
    right_cake = deque(topping)
    right_cake_dict = Counter(topping)

    while right_cake:
        topping = right_cake.popleft()

        left_cake.add(topping)

        right_cake_dict[topping] -= 1

        if right_cake_dict[topping] == 0:
            del right_cake_dict[topping]

        if len(left_cake) == len(right_cake_dict.keys()):
            answer += 1

    return answer
