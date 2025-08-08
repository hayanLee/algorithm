# https://www.acmicpc.net/problem/1253
# 투포인터, 이분 탐색

# 어떤 수가 다른 2개의 수의 합으로 나타낼 수 있을때
# 동일한 숫자가 있을때 위치가 다르면 다른 숫자

n = int(input())
nums = list(map(int,input().split()))
# n = 10
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums.sort() # 오름차순 정렬
good_cnt = 0

for i in range(len(nums)):
  target = nums[i]

  left_idx = 0
  right_idx = len(nums)-1

  while left_idx < right_idx:
    sum_left_right = nums[left_idx] + nums[right_idx] #두 수의 합을 구함

    # 다른 두 수의 합으로 자기 자신을 포함하면 넘기기
    if left_idx == i: 
      left_idx+=1
      continue
    if right_idx == i:
      right_idx-=1
      continue

    if sum_left_right == target:
      good_cnt +=1
      break
    if sum_left_right < target: #조사하는 값이 더 크면 -> 작은 값을 올려
      left_idx+=1
    elif sum_left_right > target:  # 더 작으면 -> 큰 값을 내려
      right_idx-=1
  
print(good_cnt)


