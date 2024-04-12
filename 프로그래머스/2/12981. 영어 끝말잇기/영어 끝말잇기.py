def solution(n, words):
    s = set() # 지나간 단어 담기
    prev = words[0][0] #마지막 단어의 마지막 글자 (초기화는 처음 글자)
    
    for idx, value in enumerate(words):
        if value in s or value[0] != prev: #틀림
            return [(idx % n)+1, (idx // n)+1] #[틀린 사람, 몇번째 반복]
        s.add(value)
        prev = value[-1] #마지막 글자 갱신
    return [0,0]