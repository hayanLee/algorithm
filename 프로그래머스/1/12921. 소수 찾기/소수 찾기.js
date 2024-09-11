function findPrimes(n){
    if(n<2) return 0; // 0,1은 미리 제외
    
    const arr = Array(n+1).fill(true) // 에라토스테네스의 체
    arr[0] = arr[1] = false; // 0,1은 미리 제외
    
    const limit = Math.sqrt(n); // 제곱근 반복 계산 막기
    for(let i = 2; i<=limit; i++){ // 2~n의 제곱까지만 확인
        if(arr[i]){ // 체크가 되어있으면 (= 소수이면) 
            for(let j=i*i; j<=n; j+=i) arr[j] = false;// 해당 값의 배수를 모두 지움(i보다 작은 배수는 이미 지워졌으므로 i의 배수부터 시작)
        }
    }
    
    return arr.reduce((primes, isPrime, idx) => {
        if(isPrime) primes.push(idx)
        return primes
    }, [])
}

function solution(n) {
    const primes = findPrimes(n);    
    return primes.length;
}