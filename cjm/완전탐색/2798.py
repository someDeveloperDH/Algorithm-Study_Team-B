N, M = map(int, input().split())
list_n = list(map(int, input().split()))
result = 0

for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      sum_N = list_n[i] + list_n[j] + list_n[k]
      if sum_N > M:
        continue
      else:
        result = max(result, sum_N)

print(result)