from collections import Counter


def solution(want, number, discount):
    answer = 0

    product_count = sum(number)

    wish_dict = dict(zip(want, number))

    for idx in range(len(discount) - product_count + 1):
        product = discount[idx]

        if wish_dict.get(product):
            subset_list = discount[idx : idx + product_count]

            subset_dict = Counter(subset_list)

            if subset_dict == wish_dict:
                answer += 1

    return answer
