def solution(arr):
    answer = []
    
    for x in arr:
        if(not len(answer) or answer[-1] != x): answer.append(x)
    
    return answer