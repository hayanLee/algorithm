def solution(n, m, section):
    answer = 0
    
    last_painted = -1 #가장 마지막으로 칠한 구간
    
    for start in section: # 칠할 시작 지점
        if start > last_painted:
            last_painted = start + m - 1
            answer+=1
        
    return answer