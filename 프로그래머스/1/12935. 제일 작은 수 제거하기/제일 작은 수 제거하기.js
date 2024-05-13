function solution(arr) {
    var answer = [];
    if(arr.length > 1){
        answer = arr.filter(item => item !== Math.min.apply(null, arr))
    }else{
        answer.push(-1)
    }
    return answer;
}