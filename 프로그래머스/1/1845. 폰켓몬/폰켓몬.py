def solution(nums):
    nums_set = set(nums)
    
    k = len(nums)//2 #가져갈 수 있는 마리
    
    return min(k, len(nums_set))