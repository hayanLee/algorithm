def solution(n):
    a = str(bin(n)[2:]).count("1") # 대상
    for i in range(n+1, 1_000_001):
        b = str(bin(i)[2:]).count("1")
        if a == b:
            return i