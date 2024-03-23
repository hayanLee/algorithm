#오큰수
n = int(input())
data = list(map(int, input().split()))

st = []
result = [0 for _ in range(n)]

result[-1] = -1
for i in range(len(data)-2, -1, -1):
    st.append(data[i+1])

    while len(st) > 0 and st[-1] <= data[i]:
        st.pop()
    if len(st) == 0:
        result[i] = -1
    else:
        result[i] = st[-1]

print(*result)
    #자신의 차례 때 자기 오른쪽 값을 st에 넣음
    #자기보다 작으면 pop
    #크면 오큰수
    #st이 비면 -1
