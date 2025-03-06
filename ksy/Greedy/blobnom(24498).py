n = int(input())
arr = list(map(int, input().split()))

ans = max(arr)
for i in range(1, n-1):
    if arr[i-1] >= 1 and arr[i+1] >= 1:
        a = min(arr[i-1], arr[i+1])
        b = a + arr[i]
        if b > ans:
            ans = b

print(ans)
