def solution(bandage, health, attacks):
    t,x,y = bandage # 시전 시간, 회복량, 추가 회복량
    hp = health # 체력
    heal_time = 0 # 연속 시간
    attack_idx = 0 # 공격 인덱스
    
    for time in range(1, attacks[-1][0] + 1):
        if attacks[attack_idx][0] == time: # 공격 있는지 확인
            heal_time = 0 # 연속 시간 초기화
            hp -= attacks[attack_idx][1] # 공격
            attack_idx+=1 # 다음 공격 인덱스 참조
            if hp <= 0: 
                return -1
        else: # 붕대 회복
            heal_time +=1
            hp += x
            
            if heal_time == t:
                hp += y
                heal_time = 0
            if hp >= health: # 최대 체력까지만 회복
                hp = health
        
    return hp