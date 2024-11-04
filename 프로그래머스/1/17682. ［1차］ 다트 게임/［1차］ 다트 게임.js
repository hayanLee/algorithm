function solution(dartResult) {
    const tmp = []; // 각 회차마다 점수를 저장
    
    for(let i=0; i<dartResult.length; i++){
        let ch = dartResult[i];
        if(isNum(ch)) { // 숫자
            if(ch === '1' && dartResult[i+1] === '0'){ // 10일때
                tmp.push(10)
                i++ // 0 건너뛰기
                continue
            }
            tmp.push(parseInt(ch))
        }
        else if(isUpper(ch)) { // 대문자(S,D,T)
            let num = tmp.pop()
            switch(ch) {
                case 'S':
                    tmp.push(num)
                    break;
                case 'D':
                    tmp.push(num**2) 
                    break;
                case 'T':
                    tmp.push(num**3) 
                    break;
            }
        } else {// *, #
            if(ch === '*'){
                let last = tmp.pop() * 2
                if(tmp.length > 0){ // 첫번째 숫자가 아닐 때
                    let prev = tmp.pop() * 2
                    tmp.push(prev)
                }
                tmp.push(last)
            }
            else{
                console.log(tmp)
                let last = tmp.pop() * (-1)
                tmp.push(last)
            }
        }
    }
    return tmp.reduce((a,c) => a+c)
}
    
function isNum(char){
    const code = char.charCodeAt(0);
    return code >= 48 && code <= 57;
}

function isUpper(char){
    const code = char.charCodeAt(0);
    return code >= 65 && code <= 90;
}