# (lts[i] >= h) >= h
# h > 나머지 논문 
def solution(citations):
    answer = 0
    n = len(citations)
    lts = sorted(citations, reverse=True) # 인용횟수 내림차순 정렬 
    
    for i in range(n):
        if lts[i] >= i+1:
            answer+=1
        else: # 해당 값보다 작으면 나머지 값들은 모두 다 작으므로
            break
            
    print(lts)
    return answer