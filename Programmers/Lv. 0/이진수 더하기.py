def solution(bin1, bin2):
    number = int(bin1, 2) + int(bin2, 2)
    
    return bin(number)[2:]