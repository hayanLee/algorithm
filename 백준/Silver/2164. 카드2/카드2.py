from collections import deque

arr = [i+1 for i in range(int(input()))]
dq = deque() #초기화
dq.extend(arr) # 요소 한번에 넣기

while len(dq)!=1:
  dq.popleft()
  dq.rotate(-1) #최상위꺼 빼고

print(dq[0])