n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# def bfs(x, y):
#     q = deque([(x, y)])
#     graph[x][y] = 0  # 방문처리
#     global cnt  # 해당 단지 집 개수

#     while q:
#         tmpX, tmpY = q.popleft()
#         for k in range(4):  # 방문 가능 순회
#             nx = tmpX + dx[k]
#             ny = tmpY + dy[k]

#             # 그래프 범위 + 집
#             if nx >= 0 and ny >= 0 and nx < n and ny < n and graph[nx][ny] == 1:
#                 graph[nx][ny] = 0  # 넣을 때 방문 처리
#                 cnt += 1
#                 q.append((nx, ny))

def dfs(x, y):
    # 종료조건 = 해당 위치가 집이 아닐 때
    if graph[x][y] == 0:
        return
    # 반복조건
    else:
        global cnt
        cnt += 1
        graph[x][y] = 0  # 방문처리

        for k in range(4):  # 4방향 돌면서 집 확인
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위 내 + 집
            if nx >= 0 and ny >= 0 and nx < n and ny < n and graph[nx][ny] == 1:
                dfs(nx, ny)


result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:  # 집이 있으면 시작
            cnt = 0
            dfs(i, j)
            result.append(cnt)

print(len(result))
for i in sorted(result):
    print(i)
