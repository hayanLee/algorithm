from collections import deque
n,k = map(int, input().split())

deq = deque([i+1 for i in range(n)])
res = []
while len(deq):
  deq.rotate(-(k-1))
  res.append(deq.popleft())
print(f'<{", ".join(map(str, res))}>')
