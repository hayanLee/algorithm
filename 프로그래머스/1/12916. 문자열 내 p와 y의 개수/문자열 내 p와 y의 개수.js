function solution(s){
    var result = true
    s = s.toLowerCase()
    
    cnt1 = 0
    cnt2 = 0
    for(let i=0; i<s.length; i++){
        if(s[i]==='p') cnt1++;
        else if(s[i]==='y') cnt2++;
    }
    result = cnt1===cnt2 ? true : false
    
    return result
}