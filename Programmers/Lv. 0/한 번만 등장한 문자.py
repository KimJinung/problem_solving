def solution(s):
    str_list = []
    
    for ch in s:
        if s.count(ch) == 1:
            str_list.append(ch)
    
    return ''.join(sorted(str_list))