function solution(sizes) {
    var answer = 0;
    const maxs = []
    const mins = []
    for(let i=0; i<sizes.length; i++){
        maxs.push(Math.max(...sizes[i]))
        mins.push(Math.min(...sizes[i]))
    }
    return Math.max(...maxs) * Math.max(...mins);
}