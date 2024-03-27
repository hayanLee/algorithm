from collections import deque
def bfs(maps, x,y):
    q = deque([(x,y)]) #시작 위치
    
    while q:
        tmpX, tmpY = q.popleft()
        for i in range(4):
            nx = tmpX + dx[i]
            ny = tmpY + dy[i]
            
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1: #갈 수 있음
                q.append((nx, ny))
                dist[nx][ny] = dist[tmpX][tmpY]+1 #거리 기록
                maps[nx][ny] = 0 #방문 기록
        

def solution(maps):
    answer = 0
    global dx,dy,n,m, dist
    
    dx = [0, 0, 1,-1] #동서남북
    dy = [1,-1, 0, 0]
    
    n = len(maps) #가로
    m = len(maps[0]) #세로
    
    dist = [[0]*m for _ in range(n)]
    
    bfs(maps, 0,0)
    print(dist)
    
    if dist[n-1][m-1] == 0:
        return -1
    else:
        return dist[n-1][m-1]+1