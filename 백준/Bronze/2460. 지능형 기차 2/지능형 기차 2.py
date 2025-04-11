sum = 0 # 현재 인원
max = 0 #최대 인원
for _ in range(10):
  a, b = map(int, input().split()) # 내린 사람 ,탄 사람
  sum = sum-a+b
  if max<sum: max=sum
print(max)

