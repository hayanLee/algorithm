function solution(citations) {
    citations.sort((a,b) => b-a); // 내림차순 정렬
    
    for(let h=0; h<citations.length; h++){
        if(citations[h] <= h) return h
    }
    return citations.length
}