def solution(n):
    answer = n + 1

    while True:
        zero_count_of_n = get_zero_count_by_binary(n)
        zero_count_of_next_n = get_zero_count_by_binary(answer)

        if zero_count_of_n == zero_count_of_next_n:
            return answer

        answer += 1

    return answer


def get_zero_count_by_binary(num: int) -> int:
    binary_number = bin(num)

    return binary_number.count("1")
