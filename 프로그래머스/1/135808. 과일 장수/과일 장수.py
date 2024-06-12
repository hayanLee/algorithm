def solution(k, m, score):
    answer = 0
    box = len(score) // m 
    apples = sorted(score)[len(score)%m:]
    
    for i in range(0, len(apples), m):
        answer += apples[i] * m
    return answer