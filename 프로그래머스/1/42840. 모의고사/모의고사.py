def solution(answers):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    score = [0] * 3 #각 학생의 점수
    
    for idx, answer in enumerate(answers): #문제 번호, 답
        for j, pattern in enumerate(patterns): #학생, 해당 학생 답 패턴
            if answer == pattern[idx % len(pattern)]: #답 == 패턴[문제번호 % 패턴길이]
                score[j]+=1
    
    max_score = max(score)
    answer = []
    for idx, x in enumerate(score):
        if x == max_score:
            answer.append(idx+1)
    return answer