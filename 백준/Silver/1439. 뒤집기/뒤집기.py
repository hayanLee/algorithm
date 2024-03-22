# 뒤집기
data = input()
count_zero = 0
count_one = 0

if int(data[0]) == 1:
    count_zero = 1
else:
    count_one = 1

for i in range(len(data)-1):
    if int(data[i]) != int(data[i+1]):  # 다를 때 변경 (같으면 한번에 변경하기 위해 다음으로 넘어감)
        if int(data[i+1]) == 1:
            count_zero += 1
        else:
            count_one += 1

result = min(count_one, count_zero)
print(result)
