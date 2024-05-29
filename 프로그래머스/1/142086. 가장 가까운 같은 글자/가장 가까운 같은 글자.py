def solution(s):
    answer = []
    dict = {}
    for idx, ch in enumerate(s):
        if idx == s.find(ch): 
            answer.append(-1)
        else:
            answer.append(idx - dict.get(ch))
        dict[ch] = idx
    return answer