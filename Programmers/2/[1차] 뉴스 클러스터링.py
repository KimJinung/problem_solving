def solution(str1, str2):
    intersection = 0
    union = 0

    subset_str1 = get_subset_from_string(str1.lower())
    subset_str2 = get_subset_from_string(str2.lower())

    for subset in set(subset_str1 + subset_str2):
        intersection += min(subset_str1.count(subset), subset_str2.count(subset))

        union += max(subset_str1.count(subset), subset_str2.count(subset))

    if not union:
        return 65536

    return int(intersection / union * 65536)


def get_subset_from_string(string: str) -> list:
    result = []

    for i in range(len(string) - 1):
        subset = string[i : i + 2]

        if len(subset) == 2 and subset.isalpha():
            result.append(subset)

    return result
