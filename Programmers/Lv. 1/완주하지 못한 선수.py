def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i, _ in enumerate(completion):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]


"""
문제 분류는 Hash이지만, Sort를 사용하는 케이스가 제일 먼저 떠올랐다.

1. Python의 sort는 tim sort로 O(nlogn)의 시간 복잡도를 가진다.
2. 참가자와 완료자 리스트를 모두 정렬 O(nlogn)
3. 인덱스 태워서 비교하고 다르면 반환. 끝까지 같은 경우 마지막 인원을 반환한다.
"""


# Hash를 이용한 풀이
def solution2(participant, completion):
    participant_dict = {name: 0 for name in participant}

    for name in participant:
        participant_dict[name] += 1

    for name in completion:
        participant_dict[name] -= 1

    for name, count in participant_dict.items():
        if count != 0:
            return name
