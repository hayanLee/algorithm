def calcPS(ch):
  stack = []
  for i in range(len(ch)):
    if ch[i] == '(':
      stack.append('(')
    else :
      if len(stack) and stack[-1] == '(':
        stack.pop()
      else:
        return 'NO'
  if len(stack): return 'NO'
  return "YES"

T = int(input())
for _ in range(T):
  str = input()
  print(calcPS(str))
