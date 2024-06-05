function solution(s){
     var answer = true;
     let st = 0;
    
    for(let i=0; i<s.length; i++){
        s[i] === '(' ? st++ : st--;
        if(st<0) return false; 
    }

    return answer = (st === 0) ? true : false;
}