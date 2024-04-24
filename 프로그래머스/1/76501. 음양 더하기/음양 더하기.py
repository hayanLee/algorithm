def solution(absolutes, signs):
    answer = []
    for num, sign in zip(absolutes, signs):
        if sign == False:
            answer.append(-num)
        else:
            answer.append(num)
    return sum(answer)