T = int(input())
for _ in range(T):
  R, S = input().split()

  for ch in list(S):
    print(ch*int(R), end="")
  print()
