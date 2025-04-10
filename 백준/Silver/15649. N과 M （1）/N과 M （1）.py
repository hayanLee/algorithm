from itertools import permutations
n,m = map(int, input().split())
lts = [str(i+1) for i in range(n)]

for cb in list(permutations(lts, m)):
  print(" ".join(cb))