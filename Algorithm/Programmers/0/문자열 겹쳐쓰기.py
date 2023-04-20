def solution(my_string, overwrite_string, s):
    prefix = my_string[:s]
    suffix = my_string[s + len(overwrite_string) :]

    return prefix + overwrite_string + suffix
