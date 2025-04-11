#1 22 333 4444 55555 ... 
#1부터 시작
a,b = map(int, input().split())
lts = []

i = 1 
while len(lts) < b:
  lts += [i]*i
  i+=1

print(sum(lts[a-1:b]))