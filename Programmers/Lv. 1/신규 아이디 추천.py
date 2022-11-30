# 정규 표현식 풀이
import re


def solution2(new_id):
    new_id = new_id.lower()

    new_id = re.sub("[^\w\-\_\.]", "", new_id)

    new_id = re.sub("\.{2,1000}", ".", new_id)

    new_id = re.sub("^\.|\.$", "", new_id)

    new_id = new_id if new_id else "a"

    new_id = new_id if len(new_id) <= 15 else new_id[:15]

    new_id = re.sub("\.$", "", new_id)

    new_id = new_id if len(new_id) > 2 else new_id + new_id[-1] * (3 - len(new_id))

    return new_id


def solution(new_id):
    new_id = new_id.lower()

    new_id = remove_not_allowed_character(new_id)

    new_id = remove_continuous_dots(new_id)

    new_id = remove_start_and_end_dot(new_id)

    if not new_id:
        new_id = "a"

    new_id = cut_exceeded_name_length(new_id)

    new_id = padding_for_min_name_length(new_id)

    return new_id


def remove_not_allowed_character(new_id: str) -> str:
    filtered_new_id = ""

    for ch in new_id:
        if ch in "~!@#$%^&*()=+[{]}:?,<>/":
            continue

        filtered_new_id += ch

    return filtered_new_id


def remove_continuous_dots(new_id: str) -> str:
    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    return new_id


def remove_start_and_end_dot(new_id: str) -> str:
    start = 0
    end = len(new_id)

    if new_id[0] == ".":
        start = 1

    if new_id[-1] == ".":
        end -= 1

    return new_id[start:end]


def cut_exceeded_name_length(new_id: str) -> str:
    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id[-1] == ".":
        new_id = new_id[:-1]

    return new_id


def padding_for_min_name_length(new_id: str) -> str:
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id
