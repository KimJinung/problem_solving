import re


def solution(files):
    sort_by_number = sorted(files, key=lambda file: int(re.findall("\d+", file)[0]))

    sort_by_header = sorted(
        sort_by_number, key=lambda x: re.split("\d{1,5}", x)[0].lower()
    )

    return sort_by_header
