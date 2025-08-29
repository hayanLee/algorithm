# https://www.acmicpc.net/problem/1431
# 시리얼 번호

# 대문자, 숫자
# 1. 길이가 짧은 순
# 2. 모든 자릿수를 더해서 작은 값
# 3. 사전 순 (숫자 < 알파벳)

n = int(input())
lts = [input() for _ in range(n)]

# 문자열이 들어오면 숫자 합 계산
def sum_of_nums(string):
  return sum([int(x) for x in string if x.isdigit()])

answer = sorted(lts, key = lambda x: (len(x), sum_of_nums(x), x) )
for x in answer:
    print(x)
# print(sum_of_nums('1A2'))