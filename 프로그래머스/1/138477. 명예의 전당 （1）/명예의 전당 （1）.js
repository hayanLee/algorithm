function solution(k, score) {
    const answer = [];
    const window = [];
    
    for(let i=0; i<score.length; i++){
        if(window.length < k) window.push(score[i])
        else{
            let min = Math.min(...window)
            if(min < score[i]){
                let minIdx = window.indexOf(min)
                window.splice(minIdx,1,score[i])
            }
        }
        answer.push(Math.min(...window))
    }
    return answer;
}