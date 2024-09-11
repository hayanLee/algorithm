function solution(n) {
    var answer = 0;
    
    const arr = Array(n+1).fill(true) // 에라토스테네스의 체
    for(let i = 2; i<Math.sqrt(n)+1; i++){ // 2~n의 제곱까지만 확인
        if(arr[i]){ // 체크가 되어있으면 (= 소수이면) 
            for(let j=2; i*j<=n; j++) // 해당 값의 배수를 모두 지움
                arr[i * j] = false;
        }
    }
    
    for(let i=2; i<=n; i++){
        if(arr[i] === true) answer++
    }
    
    return answer;
}