#오큰수
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

st = []
result = [-1 for _ in range(n)]

for i in range(n):
    while st and data[st[-1]] < data[i]:
        result[st.pop()] = data[i]
    st.append(i)

print(*result)
