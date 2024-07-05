function solution(array, commands) {
    var answer = [];
    for(let i=0; i<commands.length; i++){
        let t = commands[i]
        answer.push(array.slice(t[0]-1, t[1]).sort((a,b) => a-b).at(t[2]-1))
    }
    return answer;
}