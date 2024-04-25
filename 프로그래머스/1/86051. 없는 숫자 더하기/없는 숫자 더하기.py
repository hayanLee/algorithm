def solution(numbers):
    answer = 0
    sortedNums = sorted(numbers)
    for i in range(0,10):
        if i not in sortedNums:
            answer+=i
        
    return answer