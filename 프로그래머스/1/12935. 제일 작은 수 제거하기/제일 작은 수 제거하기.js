function solution(arr) {
    var answer = [];
    const min = Math.min(...arr)
    answer = arr.length > 1 ? arr.filter(item => item!==min) : [-1]
    return answer;
}