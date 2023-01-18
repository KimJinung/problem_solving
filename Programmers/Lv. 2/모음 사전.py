from itertools import product


def solution(word):
    vowels = ["A", "E", "I", "O", "U"]

    word_list = []

    for num in range(1, 6):
        case = product(vowels, repeat=num)

        word_list.extend("".join(subset) for subset in case)

    word_list.sort()

    return word_list.index(word) + 1
