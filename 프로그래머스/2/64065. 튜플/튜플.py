def solution(s): #문자열
    answer = []
    
    s = s[2:-2].split("},{")
    s = sorted(s, key = len)
    
    for x in s: #튜플을 하나씩 꺼내서
        for num in x.split(','): #해당 튜플을 순회
            if not int(num) in answer:
                answer.append(int(num))
            
    return answer