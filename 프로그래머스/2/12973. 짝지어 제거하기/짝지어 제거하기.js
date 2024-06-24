function solution(s){
    if(s.length % 2 !==0) return 0 // 홀수면 항상 남음
    const st = [] 
    
    for(let i=0; i<s.length; i++){
        if(!st.length || st[st.length-1] != s[i]) st.push(s[i])
        else st.pop()
    }
    
    return st.length ? 0 : 1
}