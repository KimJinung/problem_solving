def solution(s):
    answer = []

    ch_dict = {}

    for idx, ch in enumerate(s):
        last_idx = ch_dict.get(ch)

        if last_idx is None:
            answer.append(-1)
        else:
            answer.append(idx - last_idx)

        ch_dict[ch] = idx

    return answer
