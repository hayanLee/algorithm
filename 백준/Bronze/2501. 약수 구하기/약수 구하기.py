n, k = map(int, input().split())
arr = []
#약수 개수
for i in range(1, n+1):
  if(n%i==0): 
    arr.append(i)

print(arr[k-1] if len(arr)>=k else 0)