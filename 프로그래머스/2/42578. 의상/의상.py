def solution(clothes):
    answer = 1
    tb = {}
    for cloth, kind in clothes:
        tb[kind] = tb.get(kind, 0) + 1
            
    print(tb)        
    for kind in tb:
        answer *= (tb.get(kind) + 1)
        
    return answer-1