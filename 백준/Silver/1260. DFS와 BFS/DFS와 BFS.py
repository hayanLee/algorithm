from collections import deque
def dfs(graph, visited, node):
  print(node, end=" ") # 출력
  visited[node] = True # 방문 찍고

  for i in graph[node]:
    if not visited[i]:
      dfs(graph, visited, i)

def bfs(graph, visited, node):
  dq = deque([node]) # 시작 노드 넣기
  visited[node] = True

  while dq:
    target = dq.popleft()
    print(target, end=" ") # 출력
    for i in graph[target]:
      if not visited[i]:
        dq.append(i)
        visited[i] = True



N,M,K = map(int, input().split()) #정점, 간선, 시작 번호
graph = [[] for _ in range(N+1)] # 인접 리스트
visited = [False] * (N+1) #방문 배열

for _ in range(M):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, N + 1): # 오름차순으로 정렬
  graph[i].sort()

dfs(graph, visited, K) # 그래프, 방문 배열, 노드
print()

visited = [False] * (N + 1) # 다시 초기화
bfs(graph, visited, K)
  