def solution(citations):
    answer = 0
    citations.sort(reverse=True) # 내림차순 정렬
    
    for idx, value in enumerate(citations):
        if idx >= value:
            return idx
    return len(citations)