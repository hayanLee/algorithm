function solution(s){
    var answer = true;
    const splitedStr = s.toLowerCase().split('')
    
    let cntP = 0;
    let cntY = 0;
    
    splitedStr.forEach((ch)=> ch==='p' ? cntP++ : (ch==='y'? cntY++ : ''))

    return cntP === cntY;
}