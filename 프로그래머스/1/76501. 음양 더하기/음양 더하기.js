function solution(absolutes, signs) {
    var answer = 0;
    for(let i=0; i<signs.length; i++){
        let sign = signs[i] === true ? 1 : -1;
        answer+=(absolutes[i] * sign)
    }
    return answer;
}