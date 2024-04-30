def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    
    answer = [[0]*c2 for i in range(r1)]
    
    for i in range(r1): #행
        for j in range(c2):#열
            for k in range(r2):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            
    return answer