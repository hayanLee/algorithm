import sys
input = sys.stdin.readline

n = int(input());
heights = list(map(int,input().split()))
result = [0] * n
stack = [] # 인덱스 들어감

for i in range(n-1, -1, -1):
  while stack and heights[stack[-1]] < heights[i]: #스택에 인덱스가 들어있고, 그 인덱스 값보다 새로운 값이 더 높으면 => 그 탑에서 수신
    target_idx = stack.pop() # 요소 빼고
    result[target_idx] = i+1 # 해당 인덱스에 현재 타워 인덱스 + 1 넣기 
  
  stack.append(i);


print(*result)

