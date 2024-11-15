function solution(s) {
    var answer = [];
    //집합 기호 제거 후, 길이로 정렬
    const tuples = s.replace('{{', '').replace('}}', '').split("},{").sort((a,b) => a.length-b.length)
    
    tuples.forEach(tuple => {
        let splitedTuple = tuple.split(',')
        let t = splitedTuple.find(e => !answer.includes(e))
        answer.push(t) 
    })
    
    return answer.map(e => parseInt(e));
}