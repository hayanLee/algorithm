def solution(food):
    foods = [] # 한사람당 먹을 수 있는 양
    for i in range(1, len(food)):
        cnt = food[i] // 2
        if(cnt!=0): foods.append(str(i) * cnt)
    
    answer = ''.join(foods) + '0' + ''.join(reversed(foods))
    return answer