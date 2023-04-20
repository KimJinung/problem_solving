def solution(str1, str2):
    size = len(str1)

    return "".join(str1[idx] + str2[idx] for idx in range(size))
