def solution(num, k):
    str_num = str(num)

    try:
        return str_num.index(str(k)) + 1
    except:
        return -1
