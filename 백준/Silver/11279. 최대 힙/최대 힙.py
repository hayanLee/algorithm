from sys import stdin
import heapq
input = stdin.readline

n = int(input())
heap = []

for i in range(n):
  n = int(input())
  if(n==0):
    if(len(heap)): print(-heapq.heappop(heap))
    else: print(0)
  else:
    heapq.heappush(heap, -n)