# https://www.acmicpc.net/problem/9935
# 문자열 폭발 

# 풀이
# bomb를 포함하고 있으면 모든 bomb 제거 + 남은 문자열 이어붙임
# 새로 생긴 문자열에 bomb 생길 수 있음
# bomb가 없을때까지 반복 
# 남은 문자열이 없으면 FRULA 출력

# base = '12ab112ab2ab'
# bomb = '12ab'
base = input()
bomb = input()

stack = [] # 문자를 하나씩 넣어서 bomb가 완성되면 pop
for i in range(len(base)):
  stack.append(base[i]) # 문자열을 하나씩 넣음

  if len(stack) >= len(bomb) and stack[-1] == bomb[-1]: # 스택의 마지막 값이 폭팔물 마지막 값이랑 같으면 (가능성 o)
    target = ''.join(stack[-len(bomb):]) # 폭팔 문자열 길이만큼 슬라이싱
    if target == bomb:
      for _ in range(len(bomb)): 
        stack.pop()
  

if stack:
  print(''.join(stack))
else: 
  print('FRULA')