def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            binary = bin(number)[2:].split("0")[-1]

            answer.append(number + 2 ** (len(binary) - 1))

    return answer
