def solution(name, yearning, photo):
    answer = []
    dict = {name[i] : yearning[i] for i in range(len(name))}
    
    for i in range(len(photo)):
        sums = 0
        for j in range(len(photo[i])):
            sums += dict.get(photo[i][j],0)
        answer.append(sums)
    return answer