function solution(k, m, score) {
    var answer = 0;
    const box = parseInt(score.length / m)
    const out = parseInt(score.length % m)
    
    const apples = score.sort((a,b) => a-b).slice(out)
    
    for(let i=0; i<apples.length; i+=m){
        answer+= apples[i] * m
    }
    
    return answer;
}