function solution(t, p) {
    var answer = 0;
    for(let i=0; i<t.length-p.length+1; i++){
        let tmp = t.slice(i, i+p.length)
        if(parseInt(tmp) <= parseInt(p)) answer++
    }
    return answer;
}