from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  binary = bin(n)[2:]
  for i in range(len(binary)):
    if binary[-1 - i]=='1': #비트는 아래서부터 0 
      print(i, end=" ") 
