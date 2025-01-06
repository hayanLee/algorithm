function bfs(maps) {
    const n = maps.length; // 가로 길이
    const m = maps[0].length; // 세로 길이

    const dx = [0,1,0,-1]
    const dy = [1,0,-1,0];
    const dist = Array.from({ length: n }, () => Array(m).fill(0)); // 거리 기록
    const queue = [[0, 0]]; 
    dist[0][0] = 1; 

    while (queue.length > 0) {
        const [x, y] = queue.shift(); 

        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] === 1) {
                queue.push([nx, ny]); 
                dist[nx][ny] = dist[x][y] + 1; 
                maps[nx][ny] = 0; 
            }
        }
    }

    return dist;
}

function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;

    const dist = bfs(maps);

    if (dist[n-1][m-1] === 0) return -1;
    

    return dist[n-1][m-1];
}
