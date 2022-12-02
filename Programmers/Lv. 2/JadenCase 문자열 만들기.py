def solution(s):
    answer = ""

    is_first = True

    for ch in s:
        if ch != " ":
            if is_first:
                is_first = False

                answer += ch.upper()
            else:
                answer += ch.lower()

        else:
            is_first = True

            answer += ch

    return answer
