def solution(numbers):
    sortedNums = sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(sortedNums)))
            
    return answer