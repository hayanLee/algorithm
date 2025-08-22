# 가장 많은 종류의 폰켓몬을 선택하는 방법에서 종류 개수
def solution(nums):
    answer = 0
    pick_cnt = len(nums)//2 # 골라야하는 개수
    
    pd = {}
    for x in nums:
        pd[x] = pd.get(x, 0) + 1
        
    return min(pick_cnt, len(pd))