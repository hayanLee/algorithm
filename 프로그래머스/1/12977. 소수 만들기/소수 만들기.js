function solution(nums) {
    var answer = 0;
    for(let i=0; i<nums.length; i++){
        for(let j=i+1; j<nums.length; j++){
            for(let k=j+1; k<nums.length; k++){
                let sum = nums[i] + nums[j] + nums[k]
                if(isPrime(sum)) answer+=1
            }
        }
    }
    return answer;
}

function isPrime(n){
    for(let i=2; i<(n**0.5)+1; i++){
        if(n%i==0) return false
    }
    return true
}