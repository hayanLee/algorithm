def fibo(n):
    arr = [0,1]
    for i in range(2, n+1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[n]

def solution(n):
    answer = fibo(n)
    return answer%1234567