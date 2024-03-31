from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    
    sort_li = sorted(counter.items(), reverse =True, key = lambda x : x[1])
    
    for key,value in sort_li:
        if k<=0: break
        k-=value
        answer+=1
    return answer