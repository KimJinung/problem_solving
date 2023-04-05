from string import ascii_lowercase

SIZE = len(ascii_lowercase)


def solution(s, skip, index):
    answer = ""

    for ch in s:
        answer += decryption(ch, skip, index)

    return answer


def decryption(ch: str, exception_string: list, step: int) -> str:
    idx = ascii_lowercase.index(ch) + 1

    cnt = 0

    while cnt < step:
        idx %= SIZE

        if ascii_lowercase[idx] not in exception_string:
            cnt += 1

            if cnt == step:
                return ascii_lowercase[idx]

        idx += 1
