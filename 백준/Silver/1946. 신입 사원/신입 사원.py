#신입사원
T = int(input()) 
for _ in range(T):
    n = int(input()) #지원자 수
    data = [list(map(int, input().split())) for i in range(n)]
    data.sort(key=lambda x : x[0])

    result = 1
    target = data[0][1] # 서류 1등

    for i in range(1, len(data)):
        if target > data[i][1]: #면접 순위가 더 높으면
            result+=1
            target = data[i][1]
    
    print(result)