# 대기 인원 수
N = int(input())

# 인원 별 대기 시간
wait_times = list(map(int, input().split()))
# 인원 별 대기 시간 오름차순 정렬
wait_times.sort()

# 각 번호 별 대기 시간 합, 총 대기시간 합 구하기
wait_time = 0
total_time = 0

# 대기 시간 돌면서 하나 씩 더해주기
for time in wait_times:
    wait_time += time
    total_time += wait_time
    
print(total_time)
