from sys import stdin
input = stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key= lambda x : (x[0], x[1]))

for x in arr:
  print(x[0], x[1])