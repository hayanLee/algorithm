#1 22 333 4444 55555 ... 
#1부터 시작
a,b = map(int, input().split())
lts = []
for i in range(1,b+1): 
  for j in range(i): 
    lts.append(i)

print(sum(lts[a-1:b]))