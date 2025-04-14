from collections import deque
N, M= map(int, input().split())
graph = [list(input()) for _ in range(M)]
visited = [[False]*N for _ in range(M)] #방문 배열
# 상하좌우
dx = [-1,1,0,0];
dy=[0,0,-1,1];

b,w=0,0

def bfs(x,y):
  dq = deque([(x,y)])
  visited[x][y] = True
  cnt = 1

  while dq:
    cx, cy = dq.popleft()
    for i in range(4):
      nx = cx+dx[i]
      ny = cy+dy[i]
    
      if 0<=nx<M and 0<=ny<N and not visited[nx][ny] and graph[cx][cy] == graph[nx][ny]:
        visited[nx][ny] = True
        dq.append((nx,ny))
        cnt+=1
  return cnt


for i in range(M):
  for j in range(N):
    if not visited[i][j]:
      ans = bfs(i,j)
      if graph[i][j] == 'W':
        w+=ans**2
      else:
        b+=ans**2

print(w, b)