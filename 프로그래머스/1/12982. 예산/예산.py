def solution(d, budget):
    answer = 0
    d.sort() # 정렬
    
    for cost in d:
        if budget - cost >= 0:
            budget -= cost
            answer+=1        
    return answer