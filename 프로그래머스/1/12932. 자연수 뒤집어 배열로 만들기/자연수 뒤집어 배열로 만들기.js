function solution(n) {
    var answer = n.toString().split('').reverse();
    return answer.map(v => Number(v));
}