# 시간 초과 방지 input 설정
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

# 회의실 시간 저장
times = []
for _ in range(N):
    s, e = map(int, input().split())
    times.append((s, e))

# 회의실 시간 정렬
times = sorted(times, key=lambda x : (x[1], x[0]))

# 회의 끝나는 시간과 시작 시간을 비교하여 회의실 배정이 가능한 경우 진행
ans = 0
end = 0
for s, e in times:
    if s >= end:
        ans += 1
        end = e

print(ans)