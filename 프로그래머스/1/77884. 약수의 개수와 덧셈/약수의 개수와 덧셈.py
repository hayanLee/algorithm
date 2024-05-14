def solution(left, right):
    answer = 0
    for target in range(left, right+1): 
        # 약수 구하기
        cnt = 0 #약수 개수
        for x in range(1, target+1): #제곱근까지
            if target%x == 0: 
                cnt+=1
        if cnt%2==0: answer+=target
        else: answer-=target
    return answer