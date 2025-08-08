# https://www.acmicpc.net/problem/2110

# c개의 공유기를 '인접한 공유기간의 최소 거리'를 최대로

N,C = map(int, input().split())
house_per_distance = [int(input()) for _ in range(N)]

# N,C = 5,3 # 집, 공유기 개수
# house_per_distance = [1,2,8,4,9]
house_per_distance.sort() # 오름차순 정렬

min_dist = 1 # 최소 거리
max_dist = house_per_distance[-1] - house_per_distance[0] # 최대 거리
result = 0 # 인접 거리 중 가장 큰 값

def is_possible_to_place(distances, standard, c):
  cnt = 1 # 첫 집에서는 설치
  last_installed_idx = 0

  for i in range(1, len(distances)):
    if distances[i]-distances[last_installed_idx] >= standard: #최소 범위를 벗어나면 설치 가능
       cnt+=1
       last_installed_idx = i

  return cnt >= c


while min_dist <= max_dist:
  mid = (min_dist + max_dist) // 2 # 공유기 설치 최소 거리

  if is_possible_to_place(house_per_distance, mid, C):
      min_dist = mid + 1
      result = mid
  else:
      max_dist = mid -1 

print(result)