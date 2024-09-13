function solution(k, tangerine) {
    var answer = 0;
    const map = tangerine.reduce((acc, t) => acc.set(t, (acc.get(t) || 0) + 1), new Map());
    const sortedTangerines = [...map.entries()].sort((a, b) => b[1] - a[1]);
    
    for (const [_, count] of sortedTangerines) {
        if (k <= 0) break; 
        k -= count;        
        answer++;          
    }
    
    return answer;
}
