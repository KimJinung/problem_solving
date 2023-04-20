def solution(myString, pat):
    answer = ""
    mem = ""

    for ch in myString:
        mem += ch

        if mem.endswith(pat):
            answer = mem

    return answer
