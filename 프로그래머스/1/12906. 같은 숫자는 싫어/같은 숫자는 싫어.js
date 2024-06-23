function solution(arr){
    const st = [];
    
    for(let i=0; i<arr.length; i++){
        if(!st.length || st[st.length-1] !== arr[i]) st.push(arr[i])
    }
    
    return st;
}