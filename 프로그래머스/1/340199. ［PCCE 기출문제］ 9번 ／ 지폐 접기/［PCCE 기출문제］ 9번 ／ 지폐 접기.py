# 긴쪽을 절반으로 접기
# max(지폐) < max(지갑) and min(지폐) < min(지갑) #종료 조건
def solution(wallet, bill):
    answer = 0
    while max(bill) > max(wallet) or min(bill) > min(wallet):
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        answer+=1
    return answer