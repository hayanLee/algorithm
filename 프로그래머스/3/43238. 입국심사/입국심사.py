# 걸리는 시간 최소
def solution(n, times): #사람 수, 심사관 별 걸리는 시간
    answer = 0
    min_time = 1
    max_time = max(times) * n
    
    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2

        possible_count = sum(mid_time // t for t in times) # 각 담당관 별 mid_time에 가능한 인원 수의 합
        
        if possible_count < n:
            min_time = mid_time + 1
        else:
            max_time = mid_time - 1
            answer = mid_time

    return answer
