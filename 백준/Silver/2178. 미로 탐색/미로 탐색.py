# 미로 탐색
from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        tmpX, tmpY = q.popleft()
        for i in range(4):
            nx = tmpX+dx[i]
            ny = tmpY+dy[i]
            if nx >= 0 and ny >= 0 and nx < N and ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[tmpX][tmpY]+1
                q.append((nx, ny))

    return graph[N-1][M-1]


print(bfs(0, 0))
