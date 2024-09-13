function solution(k, tangerine) {
    var answer = 0;
    const map = new Map();
    
    tangerine.forEach(t => {
        if(map.has(t)) map.set(t, map.get(t)+1)
        else map.set(t, 1)
    })
    const sortedMap = [...map].sort((a, b) => b[1] - a[1]);
    
    for(let i=0; i<sortedMap.length; i++){
        if(k<=0) break;
        k-=sortedMap[i][1]
        answer+=1;
    }
        
    return answer;
}