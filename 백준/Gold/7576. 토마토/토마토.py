# 토마토
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()  # 큐
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            q.append((i, j))  # 처음 토마토 위치 큐에 넣기


def bfs():
    while q:
        tmpX, tmpY = q.popleft()
        for k in range(4):
            nx = tmpX + dx[k]
            ny = tmpY + dy[k]

            # 그래프 범위 내 & 벽이 아니면
            if nx >= 0 and ny >= 0 and nx < m and ny < n and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = graph[tmpX][tmpY] + 1  # 이전 날짜 + 1


bfs()  # 탐색 실행

flag = True

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            flag = False
            break

if (flag):
    print(max(max(row) for row in graph) - 1)
else:
    print(-1)
