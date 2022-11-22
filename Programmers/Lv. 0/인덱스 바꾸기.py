def solution(my_string, num1, num2):
    ch_list = list(my_string)
    ch_list[num1], ch_list[num2] = ch_list[num2], ch_list[num1]

    return "".join(ch_list)
