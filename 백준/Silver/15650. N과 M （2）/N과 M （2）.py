from itertools import combinations
n, m = map(int, input().split())
lts = [str(i+1) for i in range(n)]

for cb in list(combinations(lts, m)):
  print(" ".join(cb))
