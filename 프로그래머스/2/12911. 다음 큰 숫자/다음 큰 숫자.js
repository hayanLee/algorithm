function solution(n) {
    var answer = 0;
    
    const cnt = countOne(n)
    for(let i=n+1; i<1000000; i++){
        if(cnt === countOne(i)) return i
    }
    return answer;
}
    
function countOne(x){
    return String(x.toString(2)).split('').filter((t) => t==='1').length
}