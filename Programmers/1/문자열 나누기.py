def solution(s):
    answer = 0

    subset = s

    while True:
        subset = get_subset_by_condition(subset)

        answer += 1

        if not subset:
            break

    return answer


def get_subset_by_condition(s: str) -> str:
    x_count = 0
    y_count = 0

    for idx, ch in enumerate(s):
        if ch == s[0]:
            x_count += 1
        else:
            y_count += 1

        if x_count == y_count:
            return s[idx + 1 :]

    return ""
