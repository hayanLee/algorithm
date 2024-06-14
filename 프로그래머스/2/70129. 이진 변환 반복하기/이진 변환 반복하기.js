function solution(s) {
    let cnt = 0 // 변환 횟수
    let zero = 0 //제거한 0 개수
    
    while(s!=='1'){
        let current = s.split('').filter(t => t==='0').length
        zero+=current
        
        s=s.replaceAll('0', '') // 0제거
        
        let length = s.length
        
        s = String(length.toString(2))
        
        cnt+=1
    }
    
    return [cnt, zero];
}