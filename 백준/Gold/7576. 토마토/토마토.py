#토마토
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

q = deque()

def bfs():
    while q:
        tmpX, tmpY = q.popleft()
        for i in range(4):
            nx = tmpX + dx[i]
            ny = tmpY + dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0: #범위 내 and 방문 안함
                q.append((nx,ny))
                dist[nx][ny] = dist[tmpX][tmpY]+1 #현재 거리 +1
                graph[nx][ny] = -1 #방문 처리

m,n = map(int, input().split()) #세로 가로
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[0]*m for _ in range(n)] # 거리 리스트

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dist[i][j] = 1
            q.append((i,j)) #시작하는 곳 큐에 넣기

bfs()

flag = True
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = False
            break

if flag:
    print(max(max(row) for row in dist) - 1)
else:
    print(-1)
