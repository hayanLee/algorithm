def solution(n):
    answer = sum([int(str(n)[i]) for i in range(len(str(n)))])
    return answer