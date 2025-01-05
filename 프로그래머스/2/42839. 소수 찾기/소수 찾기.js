function isPrime(n){
    if(n < 2) return false
    for(let i=2; i<=Math.sqrt(n); i++){
        if(n%i === 0) return false
    }
    return true
}

function dfs(nums, set, cur){
    if (cur !== '') {
        let num = parseInt(cur);
        if (isPrime(num)) set.add(num);  
    }
 
    for (let i = 0; i < nums.length; i++) {
        let newCur = cur + nums[i];  
        let remaining = nums.slice(0, i).concat(nums.slice(i + 1));  
        dfs(remaining, set, newCur);  
    }
}

function solution(numbers) {
    var answer = 0;
    const nums = numbers.split('')
    let set = new Set(); 
    
    dfs(nums, set, '')
    return set.size;
}