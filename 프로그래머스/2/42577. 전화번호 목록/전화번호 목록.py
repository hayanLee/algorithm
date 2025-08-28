# 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
def solution(phone_book):
    answer = True
    sorted_lts = sorted(phone_book) 
    
    for i in range(len(sorted_lts)-1):
        if sorted_lts[i+1].startswith(sorted_lts[i]):
            return False
    return answer