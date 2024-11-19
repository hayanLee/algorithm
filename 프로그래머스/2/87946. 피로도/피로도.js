function solution(k, dungeons) {
    var answer = 0;
    const visited = Array(dungeons.length).fill(false)
    
    const dfs = (hp, cnt) => {
        for(let i=0; i<dungeons.length; i++){
            if(!visited[i] && hp >= dungeons[i][0]){
                visited[i] = true
                dfs(hp-dungeons[i][1], cnt+1);
                visited[i] = false
            }
        }
        answer = Math.max(answer, cnt)
    }
    
    dfs(k, 0)
    return answer;
}

