def solution(n):
    answer = 0
    for i in range(1, n+1): #시작점
        sum = 0 
        for j in range(i, n+1): #더할 요소
            sum+=j
            if sum == n: # 요소들의 합이 n이 되면 종료
                answer+=1
            if sum>=n:
                break
    return answer