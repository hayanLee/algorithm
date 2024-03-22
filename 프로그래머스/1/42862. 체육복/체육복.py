def solution(n, lost, reserve):
    answer = 0
    set_reserve = set(reserve)- set(lost) # 여벌 체육복을 가져온 학생이 도난 당할 수 있음
    set_lost = set(lost) - set(reserve) # 중복 제외 체육복이 없는 친구
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)