from collections import defaultdict


def solution(keymap, targets):
    answer = []

    ch_weight_dict = calcul_character_weight(keymap)

    for target in targets:
        cnt = 0

        for ch in target:
            if not ch_weight_dict.get(ch):
                cnt = -1
                break

            cnt += ch_weight_dict[ch]

        answer.append(cnt)

    return answer


def calcul_character_weight(keymap: list) -> dict:
    weight_dict = defaultdict(int)

    for button in keymap:
        for idx, ch in enumerate(button):
            idx += 1

            if weight_dict[ch] == 0:
                weight_dict[ch] = idx
            elif weight_dict[ch] > idx:
                weight_dict[ch] = idx

    return weight_dict
