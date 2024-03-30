#유기농 배추
import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

t = int(input()) #테스트 개수

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    graph[x][y] = 0 # 방문처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
            dfs(nx,ny)

# def bfs(x,y):
#     q = deque([(x,y)])
#     graph[x][y] = 0 #방문처리

#     while q:
#         tmpX, tmpY = q.popleft()
#         for i in range(4):
#             nx = tmpX + dx[i]
#             ny = tmpY + dy[i]

#             if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
#                 q.append((nx,ny))
#                 graph[nx][ny] = 0 # 방문 처리

for _ in range(t):
    n,m,k = map(int, input().split()) #가로/세로/배추개수
    graph = [[0]*m for _ in range(n)] #n*m
    cnt = 0 #총 마리 수

    for _ in range(k):
        a, b = map(int, input().split()) #배추 x, y좌표
        graph[a][b] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i,j)
                # bfs(i,j)
                cnt+=1 #탐색이 종료되면 영역 1증가
    
    print(cnt)

