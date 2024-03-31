def solution(number, limit, power):    
    answer = 0
    for n in range(1,number+1):
        #약수 개수를 구함
        length = getPrimeLength(n)
        if length <= limit:
            answer+=length
        else:
            answer+=power

    return answer

def getPrimeLength(n):
    #1~제곱근까지 약수 찾음 (약수의 대칭성으로 발견 시 2개씩 더해줌)
    #제곱수 중복 제거
    return sum(2 for i in range(1, int(n**0.5) + 1) if n % i == 0) - (int(n**0.5) ** 2 == n) 