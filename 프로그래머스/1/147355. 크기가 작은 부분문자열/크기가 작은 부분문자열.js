function solution(t, p) {
    var answer = 0;
    const lenA = t.length
    const lenB = p.length
    
    for(let i=0; i<=lenA-lenB; i++){
        if(t.substr(i, lenB) <= p) answer++
    }
    return answer;
}