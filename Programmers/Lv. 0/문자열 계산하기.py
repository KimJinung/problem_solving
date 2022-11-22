def solution(my_string):
    item_list = my_string.split()
    answer = int(item_list[0])

    for i in range(1, len(item_list), 2):
        if item_list[i] == "+":
            answer += int(item_list[i + 1])
        else:
            answer -= int(item_list[i + 1])

    return answer
