def solution(num_list, n):
    size = len(num_list)
    answer = [num_list[idx] for idx in range(0, size, n)]

    return answer
