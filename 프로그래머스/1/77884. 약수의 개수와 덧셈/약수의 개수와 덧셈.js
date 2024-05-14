function solution(left, right) {
    var answer = 0;
    for(let i=left; i<=right; i++){
        if (i**0.5 === parseInt(i**0.5)) answer-=i
        else answer+=i
    }
    return answer;
}