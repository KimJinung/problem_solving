def solution(phone_book):
    phone_book.sort(key=len, reverse=True)

    number_dict = {}

    for idx, number in enumerate(phone_book):
        if number_dict.get(number):
            return False

        if idx + 1 >= len(phone_book):
            break
        else:
            limit = len(phone_book[idx + 1])

            for i in range(limit):
                number_dict[number[0 : i + 1]] = True

    return True


# 정렬을 사용하지 않는 풀이
def solution2(phone_book):
    number_dict = {}

    for number in phone_book:
        number_dict[number] = True

    for number in phone_book:
        subset = ""

        for digit in number:
            subset += digit

            if number != subset and number_dict.get(subset):
                return False

    return True
