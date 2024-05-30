def solution(k, score):
    answer = [] #최하위 값 모음
    window = [] #명예의 전당
    
    for x in score:
        if len(window) < k:
            window.append(x)
        else: #자리 다참
            if min(window) < x:
                window.remove(min(window))
                window.append(x)
        answer.append(min(window))
        
    return answer