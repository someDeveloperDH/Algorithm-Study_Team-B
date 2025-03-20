N = int(input()) # 분해합 찾을 숫자 입력
result = 0 # 생성자 저장 변수

start = max(1, N - (len(str(N)) * 9)) # 탐색 범위

for i in range(start, N):
  total = i
  for j in str(i):
    total += int(j)
  if total == N:
    result = i
    break

print(result)