def solution(s):
    answer = ''
    for x in s.split(' '):
        for i in range(len(x)):
            if i%2==0:
                answer+=x[i].upper()
            else:
                answer+=x[i].lower()
        answer+=' '
    return answer[:-1]
