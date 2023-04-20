def solution(arr1: list, arr2: list):
    return compare_arr_size_by_domain(arr1, arr2)


def compare_arr_size_by_domain(arr1: list, arr2: list) -> int:
    size_of_arr1 = len(arr1)
    size_of_arr2 = len(arr2)

    if size_of_arr1 > size_of_arr2:
        return 1
    elif size_of_arr2 > size_of_arr1:
        return -1

    sum_of_arr1 = sum(arr1)
    sum_of_arr2 = sum(arr2)

    if sum_of_arr1 > sum_of_arr2:
        return 1
    elif sum_of_arr2 > sum_of_arr1:
        return -1

    return 0
