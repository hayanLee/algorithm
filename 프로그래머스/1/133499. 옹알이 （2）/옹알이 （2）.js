function solution(babbling) {
    var answer = 0;
    const cans = ["aya", "ye", "woo", "ma"]
    
    for(let i=0; i<babbling.length; i++){
        let str = babbling[i]
        for(let c=0; c<cans.length; c++){ 
            if(str.includes(cans[c].repeat(2))) break; // 연속 발음 안됨
            str = str.split(cans[c]).join(' ') // 해당 문자 제거 후, str 갱신
        }
        
        if(str.split(' ').join('').length === 0) answer++
    }
    return answer;
}