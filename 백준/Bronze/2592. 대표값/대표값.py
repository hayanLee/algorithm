from collections import Counter
lts = [int(input()) for _ in range(10)]
counters = Counter(lts)
print(sum(lts)//10)
print(counters.most_common(1)[0][0])