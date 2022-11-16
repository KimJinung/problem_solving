import string

def solution(age):
    alphabet = list(string.ascii_lowercase)
    
    return ''.join([alphabet[int(idx)] for idx in str(age)])
    