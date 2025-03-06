n = int(input())

arr = list(map(int, input().split()))

a = [0] * n

height = 1
for num in arr:
    cnt = -1
    for idx, i in enumerate(a):
        if i == 0:
            cnt += 1
        if cnt == num:
            a[idx] = height
            height += 1
            break

print(*a)