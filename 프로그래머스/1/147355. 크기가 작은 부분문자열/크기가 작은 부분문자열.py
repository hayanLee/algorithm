def solution(t, p):
    answer = 0
    x = len(t)
    y = len(p)
    for i in range(x-y+1):
        if(t[i:i+y] <= p): answer+=1

    return answer