def solution(price, money, count):
    # count를 횟수로 price가 배수로 증가
    cost = 0
    for i in range(1, count+1):
        cost += price * i # 내야하는 돈
    
    return 0 if cost-money < 0 else cost-money