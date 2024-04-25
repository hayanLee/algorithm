def solution(s):
    answer = ''
    strs = list(map(int, s.split()))
    first = min(strs)
    second = max(strs)
    
    answer += str(first) + " " + str(second)
    return answer