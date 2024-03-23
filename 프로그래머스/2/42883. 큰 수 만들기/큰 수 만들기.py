def solution(number, k):
    answer = []
    
    for x in number:
        while k>0 and answer and answer[-1] < x:
            answer.pop()
            k-=1
        answer.append(x)
        
    return ''.join(answer[:len(answer)-k])