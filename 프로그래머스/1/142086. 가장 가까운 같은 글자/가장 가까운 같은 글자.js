function solution(s) {
    var answer = [];
    const obj = {}
    for(let i=0; i<s.length; i++){
        if(obj.hasOwnProperty(s[i])){ // 이전에 요소 만남
            answer.push(i - obj[s[i]]) // 현재 요소 인덱스 - 이전 요소 인덱스
        }else {
            answer.push(-1) // 처음만나면 -1
        }
        obj[s[i]] = i // 현재 요소 인덱스 갱신
    }
    return answer;
}