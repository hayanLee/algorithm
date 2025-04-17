from collections import deque
a,b = map(int, input().split())

# 2 곱하기
# '1'을 마지막에 추가하기

def bfs(x,level):
  dq = deque([(x, level)])
  while dq:
    current, level = dq.popleft()
    if current == b:
      return level
    if current*2 <= b:
      dq.append((current*2, level+1))
    if int(str(current) + '1') <= b:
      dq.append((int(str(current) + '1'), level+1))
  return -1

print(bfs(a,1))