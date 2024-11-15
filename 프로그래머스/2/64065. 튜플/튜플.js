function solution(s) {
    //집합 기호 제거 후, 길이로 정렬
    const tuples = s.slice(2, -2).split("},{").sort((a,b) => a.length-b.length)
    
    const result = tuples.reduce((acc, elements) => {
        let splitedTuple = elements.split(',')
        let t = splitedTuple.find(e => !acc.includes(e))
        acc.push(t) 
        return acc
    }, [])
    
    console.log(result)
    return result.map(Number);
}