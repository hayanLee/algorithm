# https://www.acmicpc.net/problem/1874
# 스택 수열

# 1~N까지 입력
# 스택에서 pop해서 arr을 완성해야함
# push할때는 오름차순으로 (넣어야 하는 값 < 출력하는 값 => no)

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)] # [4, 3, 6, 8, 7, 5, 2, 1]
stack =[]
result = []
current = 1

for num in arr: # pop해야하는 값 
  # 순차적으로 넣는 값 <= pop해야하는 값 
  # pop하기 위해서 먼저 push
  while current <= num: 
    stack.append(current)
    result.append('+')
    current +=1 
  
  if stack[-1] == num: # 같으면 팝
    stack.pop()
    result.append('-')
  
  else: 
    print('NO')
    break

else:
  print('\n'.join(result))

