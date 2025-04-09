arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' #진법
result = 0
b, n = input().split()

for idx, v in enumerate(b[::-1]):
  result += arr.index(v) * (int(n) ** idx)
  
print(result)