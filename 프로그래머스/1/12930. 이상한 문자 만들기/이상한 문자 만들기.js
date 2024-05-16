function solution(s) {
    var answer = '';
    const newStr = s.split(' ')
    for(let i=0; i<newStr.length; i++){
        for(let j=0; j<newStr[i].length; j++){
            if(j%2==0) answer+=newStr[i][j].toUpperCase()
            else answer+=newStr[i][j].toLowerCase()
        }
        answer+=' '
    }
    return answer.slice(0,answer.length-1);
}