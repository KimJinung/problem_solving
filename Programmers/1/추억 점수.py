from collections import defaultdict


def solution(name, yearning, photo):
    photos = photo

    answer = []

    yearning_score = defaultdict(int)

    for idx in range(len(name)):
        friend = name[idx]
        score = yearning[idx]

        yearning_score[friend] = score

    for photo in photos:
        score = 0

        for friend in photo:
            score += yearning_score[friend]

        answer.append(score)

    return answer
