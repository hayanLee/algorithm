def solution(answers):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    score = [0] * 3 # 각 학생 점수
    
    for idx, answer in enumerate(answers): #문제번호, 답
        for stu, pattern in enumerate(patterns): #학생, 개인 답
            if answer == pattern[idx % len(pattern)]:
                score[stu]+=1
    
    max_score = max(score)
    result = []
    
    for idx,value in enumerate(score):
        if value == max_score:
            result.append(idx+1)
    return sorted(result)