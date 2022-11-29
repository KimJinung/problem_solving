def solution(dartResult):
    answer = []

    bonus = {"S": 1, "D": 2, "T": 3}
    option = {"*": 2, "#": -1}

    for idx, ch in enumerate(dartResult):
        if ch.isdigit():
            if idx > 0 and dartResult[idx - 1].isdigit():
                modified_num = str(dartResult[idx - 1]) + ch

                answer[-1] = int(modified_num)
            else:
                answer.append(int(ch))

        else:
            if ch in bonus.keys():
                answer[-1] **= bonus[ch]

            else:
                op = option[ch]

                if ch == "*":
                    answer[-1] *= op

                    if len(answer) > 1:
                        answer[-2] *= op

                elif ch == "#":
                    answer[-1] *= op

    return sum(answer)


# 정규 표현식을 이용한 풀이
import re


def solution2(dartResult):
    bonus = {"S": 1, "D": 2, "T": 3}
    option = {"*": 2, "#": -1, "": 1}

    r = re.compile("(\d+)([SDT])([*#]?)")
    re_dart = r.findall(dartResult)  # [('1', 'S', '#'), ('3', 'D', '')]

    for idx, _ in enumerate(re_dart):
        if re_dart[idx][2] == "*" and idx > 0:
            re_dart[idx - 1] *= 2

        re_dart[idx] = (
            int(re_dart[idx][0]) ** bonus[re_dart[idx][1]] * option[re_dart[idx][2]]
        )

    return sum(re_dart)
