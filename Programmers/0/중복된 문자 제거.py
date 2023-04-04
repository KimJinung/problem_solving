def solution(my_string):
    answer = ""
    mem = {}

    for ch in my_string:
        if mem.get(ch):
            continue
        else:
            mem[ch] = True
            answer += ch

    return answer
