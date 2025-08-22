def solution(participant, completion):
    d = {}
    
    for p in participant:
        d[p] = d.get(p,0) + 1
    
    for c in completion:
        if c in d:
            d[c] -= 1
    
    answer = [k for k,v in d.items() if v!=0]
    return answer[0]