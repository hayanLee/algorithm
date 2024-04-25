def solution(s):
    answer = []
    word = s.split(" ")
    
    for x in word:
        if x != "":
            answer.append(x[0].upper() + x[1:].lower())
        else:
            answer.append("")
    return ' '.join(answer)
