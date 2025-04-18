from collections import deque
n, k = map(int, input().split())


def bfs(start, goal):
  dq = deque([(start, 0)]) # (시작위치, 시간)
  visited = [-1] * 100001 # 방문 기록
  visited[start] = 0

  while dq:
    target, time = dq.popleft()
    if target == goal:
      return time

    for next, cost in [(target-1, 1), (target+1, 1), (target*2, 0)]:
      if 0<=next<=100000:
        next_time = time + cost
        if visited[next] == -1 or visited[next] > next_time: 
          visited[next] = next_time
          if cost == 0:
            dq.appendleft((next, time))  # 순간이동
          else:
            dq.append((next, time + 1))  # 이동
      
print(bfs(n, k))