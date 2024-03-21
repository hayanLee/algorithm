#팰린드롬인지 확인하기
front = input()
back = front[::-1]

if front == back:
    print(1)
else:
    print(0)


