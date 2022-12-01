def solution(survey, choices):
    answer = ""

    score = [0, 3, 2, 1, 0, 1, 2, 3]

    mbti = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }

    for idx, choice in enumerate(choices):
        if choice == 4:
            continue

        if choice < 4:
            indicator = survey[idx][0]

            mbti[indicator] += score[choice]
        else:
            indicator = survey[idx][1]

            mbti[indicator] += score[choice]

    for types in ["RT", "CF", "JM", "AN"]:
        type1 = types[0]
        type2 = types[1]

        type1_score = mbti[type1]
        type2_score = mbti[type2]

        if type1_score > type2_score:
            answer += type1
        elif type1_score < type2_score:
            answer += type2
        else:
            padding_type = sorted(types)[0]

            answer += padding_type

    return answer
