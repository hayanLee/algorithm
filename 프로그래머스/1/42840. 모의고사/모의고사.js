function solution(answers) {
    var answer = []; 
    const patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    const score = [0,0,0]
    
    for(let i=0; i<3; i++){ // 학생 수
       let stu = patterns[i] // i번 학생 답
       for(let j=0; j<answers.length; j++){ // 정답
           if(answers[j] === stu[j%(stu.length)]) score[i]+=1
           // console.log(`학생 ${i+1}번, 답 : ${answers[j]} 학생 답 : ${stu[j%(stu.length)]}`)
       }
    }
    
    const max = Math.max(...score)
    
    for(let i=0; i<score.length; i++){
        if(score[i] === max) answer.push(i+1)
    }
    return answer;
}