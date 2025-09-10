# 설정한 시간에 늦지 않고 출근한 직원
# 희망시간 + 10 
# 토,일 제외(6,7) -> startday
# 시*100 + 분

# (start+i - 1)%7 + 1
# start = 5 
# 0 : 4%7 + 1= 5 
# 1 : 5%7 + 1 = 6
# 2 : 6%7 + 1 = 7
# 3 : 7%7 + 1 = 1
# ..
# 6 : 10%7 + 1 = 4


# i : schedules 길이, schedule = [i]
# j : 7
def set_deadline(time, m):
    hour = time // 100
    minute = time % 100
    minute += m
    hour += minute // 60
    minute %= 60
    return hour * 100 + minute

def solution(schedules, timelogs, startday):
    answer = 0
    cnt = 0
    for i in range(len(schedules)):
        deadline = set_deadline(schedules[i], 10) # i 직원의 출근 희망 시간
        all_success = True
        for j in range(7):
            day = (startday + j - 1)%7 + 1 # 해당 날짜
            if day not in (6,7): # 토,일 제외
                if timelogs[i][j] > deadline: # 지각하면 종료
                    all_success = False 
                    break
        if all_success:
            cnt+=1
    
    return cnt