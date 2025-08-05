def solution(numbers, target):
    results = []
    cnt = 0

    def get_sum_by_using_plus_minus(index, sum):
        if index == len(numbers): #모든 수 다쓰면
            results.append(sum)
            return 

        get_sum_by_using_plus_minus(index+1, sum+numbers[index]) 
        get_sum_by_using_plus_minus(index+1, sum-numbers[index])
    
   
    get_sum_by_using_plus_minus(0,0)
    
    
    for result in results:
        if result == target:
            cnt+=1
        
    return cnt