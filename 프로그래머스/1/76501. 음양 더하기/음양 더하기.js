function solution(absolutes, signs) {
    var answer = 0;
    absolutes.forEach((item, idx) => {
        if(signs[idx]) answer+=item
        else answer-=item
    })
    return answer;
}