n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(m):
    arr.sort()
    a = arr[0] + arr[1]
    arr[0] = a
    arr[1] = a

ans = sum(arr)

print(ans)