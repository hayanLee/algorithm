function solution(x) {
    let tmp = String(x).split('').map(Number)
    let sum = tmp.reduce((a,c) => a+c)
    
    return x%sum === 0 ? true : false
}