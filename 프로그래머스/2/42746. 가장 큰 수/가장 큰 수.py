def solution(numbers):
    answer = ''
    lts = list(map(str, numbers))
    sorted_lts = sorted(lts, key = lambda x : x*3, reverse = True)
    
    answer = ''.join(sorted_lts)
    if answer[0] == '0':
        return '0'
    
    return answer