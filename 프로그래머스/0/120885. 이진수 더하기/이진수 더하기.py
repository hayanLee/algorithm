def solution(bin1, bin2): 
    sum = int(bin1, 2) + int(bin2, 2)
    answer = bin(sum)[2:]
    return answer