from itertools import combinations
#9C7 = 9C2
lts = [int(input()) for _ in range(9)] # 100보다 작은 자연수, 중복 없음
lts.sort() # 오름차순 정렬

diff = sum(lts)-100 # 모든 합
if diff: # 딱 100
  for comb in combinations(lts, 2):
    if sum(comb) == diff:
      for val in comb:
        lts.remove(val)
      break;
for i in lts: print(i)