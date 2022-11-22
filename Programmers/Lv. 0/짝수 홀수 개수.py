def solution(num_list):
    even_number = [num for num in num_list if num % 2 == 0]
    even_length = len(even_number)

    return [even_length, len(num_list) - even_length]
