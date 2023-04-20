def solution(num_list):
    negative_num_list = [num for num in num_list if num < 0]

    if negative_num_list:
        first_negative_num = negative_num_list[0]
        return num_list.index(first_negative_num)

    return -1
