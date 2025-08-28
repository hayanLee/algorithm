# i번째 숫자부터 j번째 숫자까지 자르고 정렬 후 -> k번째 수
def solution(array, commands):
    answer = []
    
    for T in range(len(commands)):
        i,j,k = commands[T]
        lts = sorted(array[i-1:j])
        # print(lts)
        answer.append(lts[k-1])
    return answer