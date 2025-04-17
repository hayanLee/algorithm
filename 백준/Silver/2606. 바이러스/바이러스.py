n = int(input()) # 컴퓨터
m = int(input()) # 연결 개수

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) # 방문 배열
res = 0

def dfs(x):
  visited[x] = True
  cnt = 0 # 새로 방문할 때 추가하고, 자기는 안셈(1은 제외니까)

  for node in graph[x]:
    if not visited[node]:
      cnt += 1
      cnt += dfs(node)
  return cnt

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

res += dfs(1)
print(res)

