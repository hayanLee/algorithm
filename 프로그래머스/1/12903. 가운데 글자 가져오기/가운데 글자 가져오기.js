function solution(s) {
    let delIdx = parseInt(s.length/2)
    if(Number.isInteger(s.length/2)){ 
        return s.slice(delIdx-1, delIdx+1)
    }else{
        return s[delIdx]
    }
}