from collections import deque
n,m,k = map(int, input().split()) #세로, 가로, 쓰레기 개수
graph = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
  i,j = map(int, input().split())
  graph[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# def dfs(x,y):
#   cnt = 1
#   graph[x][y] = 0 #방문처리
#   for i in range(4):
#     nx, ny = x + dx[i], y+dy[i]
#     if 1<=nx<n+1 and 1<=ny<m+1 and graph[nx][ny]==1:
#       cnt += dfs(nx, ny)
#   return cnt

def bfs(x,y):
  cnt = 1
  dq = deque([(x,y)])
  graph[x][y] = 0 # 방문 처리
  
  while dq:
    cx, cy = dq.popleft()

    for i in range(4):
      nx, ny = cx+dx[i], cy+dy[i]
      if 1<=nx<n+1 and 1<=ny<m+1 and graph[nx][ny]==1:
        cnt+=1
        graph[nx][ny]=0
        dq.append((nx,ny))
  return cnt

max = -1e9
cnt = 0
for i in range(1,n+1):
  for j in range(1,m+1):
    if graph[i][j]: 
      cnt = bfs(i,j)
      if max < cnt : max = cnt

print(max)
