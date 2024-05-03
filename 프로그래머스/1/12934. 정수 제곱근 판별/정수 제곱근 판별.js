function solution(n) { 
    if(n**0.5 % 1 === 0){
        let tmp = n**0.5
        return (tmp+1)**2
    }
    return -1
}