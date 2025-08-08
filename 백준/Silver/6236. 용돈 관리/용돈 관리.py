# https://www.acmicpc.net/problem/6236
# 이분 탐색

# 정확히 m번 인출 (고정 금액 k원 인출)
# k원 인출 >> 부족하면 남은 금액 재 입금 후 k원 인출
# 남은 금액이 많더라도 m회를 맞추기 위해 입금 후 재입출

# k 최소화

n,m = map(int, input().split())
daily_spending = [int(input()) for _ in range(n)]

def is_possible(daily_expenses, max_withdraw_amount, max_withdraw_count):
    withdraw_count = 1  # 첫 인출
    remaining_cash = 0  # 현재 가진 돈

    for expense in daily_expenses:
        if remaining_cash + expense > max_withdraw_amount: # 현재 가진 돈 + 오늘 쓸 돈 > 인출 한도 → 새로 인출
            remaining_cash = 0
            withdraw_count += 1
        remaining_cash += expense  # 오늘 쓸 돈 챙기기

    return withdraw_count <= max_withdraw_count

# n,m=7,5
# daily_spending = [100, 400, 300, 100, 500, 101, 400]
min_k = max(daily_spending) # 하루에 쓰는 금액 중 최대값
max_k = sum(daily_spending) # 총액

while min_k <= max_k:
    mid_k = (min_k + max_k) // 2 # 중앙값

    if is_possible(daily_spending, mid_k, m):
        answer = mid_k  # mid_k는 조건을 만족하므로 최소값 후보가 됨
        max_k = mid_k - 1  # 더 작은 K가 있는지 왼쪽 탐색
    else:
        min_k = mid_k + 1  # 인출 횟수가 부족하므로 오른쪽 탐색

print(answer)