function solution(word) {
    var answer = 0;
    const vowels = ['A', 'E', 'I', 'O', 'U']
    let flag = false
    
    const def = (cur) => {
        if(cur.length > 5 || flag) return 
        
        if(cur === word){
            flag = true
            console.log('찾음', cur, word, answer)
            return
        }
        
        answer++;
        
        for(let i=0; i<vowels.length; i++){
            def(cur + vowels[i])
        }
    } 
    
    def('')
    return answer;
}