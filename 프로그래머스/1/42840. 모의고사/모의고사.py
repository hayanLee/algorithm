def solution(answers):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    score = [0] * 3 # 각 학생 점수
    
    for idx, answer in enumerate(answers): #문제번호, 답
        for stu in range(3): #3명의 학생
            if answer == patterns[stu][idx%len(patterns[stu])]:
                score[stu]+=1
            # print(answer, stu, patterns[stu][idx%len(patterns[stu])])
    
    max_score = max(score)
    result = []
    
    for idx,value in enumerate(score):
        if value == max_score:
            result.append(idx+1)
    return sorted(result)