n, m = map(int, input().split()) #가로 크기, 세로 크기
graph = [list(input()) for _ in range(m)]
visited = [[False]*n for _ in range(m)] # 방문 배열

w,b = 0,0

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1] 

def dfs(x,y,team):
  cnt = 1
  visited[x][y] = True # 방문처리

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] == team:
      cnt += dfs(nx,ny,team)
  
  return cnt

for i in range(m):
  for j in range(n):
    if not visited[i][j]:
      if graph[i][j] == 'W':
        w+=dfs(i,j,'W')**2
      else:
        b+=dfs(i,j,'B')**2

print(w,b)