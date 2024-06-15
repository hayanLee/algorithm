function solution(n, m, section) {
    var answer = 0;
    
    let last_start = -1; 
    
    for(start of section){
        if(start > last_start){
            last_start = start + m - 1;
            answer+=1            
        }
    }
        
    
    return answer;
}