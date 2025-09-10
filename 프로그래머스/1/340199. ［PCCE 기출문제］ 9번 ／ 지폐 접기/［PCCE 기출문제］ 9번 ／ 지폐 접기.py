# 지폐 큰쪽 절반 접기 < 90도 돌리기
def solution(wallet, bill):
    answer = 0
    n = len(wallet) # 2
    
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] > bill[1]: # 가로 > 세로
            bill[0] = bill[0]//2
        else:
            bill[1] = bill[1]//2
        answer+=1
        
    return answer