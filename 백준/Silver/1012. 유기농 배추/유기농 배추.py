import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 해제
input = sys.stdin.readline

# 방향 벡터 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 재귀 DFS
def dfs_recur(x, y):
    graph[y][x] = 0  # 방문 처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
            dfs_recur(nx, ny)

# 스택 DFS
def dfs_stack(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if graph[cy][cx] == 1:  # 아직 방문 안 했으면
            graph[cy][cx] = 0
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
                    stack.append((nx, ny))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())  # M=가로, N=세로
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1  # 좌표 저장 (행=y, 열=x)

    worm_cnt = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                dfs_recur(x, y)
                # dfs_stack(x, y)
                worm_cnt += 1

    print(worm_cnt)
