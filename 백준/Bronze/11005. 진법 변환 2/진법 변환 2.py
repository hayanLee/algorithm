arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' #진법
result = ''

n,b = map(int, input().split())

while n:
  result += str(arr[n%b]) #나눈 나머지의 인덱스
  n//=b
print(result[::-1]) #역순