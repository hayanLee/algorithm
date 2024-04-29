from itertools import combinations
def solution(number):
    answer = 0
    
    for combo in combinations(number, 3):
        if sum(combo) == 0: answer+=1

    return answer