def solution(numbers):
    numbers_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    answer = ""
    num_str = ""

    for ch in numbers:
        num_str += ch

        value = numbers_dict.get(num_str)

        if value:
            answer += str(value)
            num_str = ""

    return int(answer)
