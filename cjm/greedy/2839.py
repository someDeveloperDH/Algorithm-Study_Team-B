N = int(input())

answer = 0

if N % 5 == 0:
    print(N // 5)
else:
    while N > 0:
        # N에 3을 계속 빼주면서, 3을 하나씩 답에 더해주고
        # 5로 나눠지는 지 확인
        N -= 3
        answer += 1
        # 만약 13과 같은 경우 3을 한번 빼면 다음 값이 10인데
        # 이건 5로 나뉘어 떨어지기 때문에 바로 answer에 더해서 출력
        if N % 5 == 0:
            answer += N // 5
            print(answer)
            break
        # 만약 N을 계속 빼다가 1 또는 2가 나와서 0보다 작아지는 경우
        # -1을 return 하여 나눌 수 없음을 표현
        elif N == 1 or N == 2:
            print(-1)
            break
        elif N == 0:
            # 만약 3으로 계속 나뉘어 떨어지는 경우 answer가 계속 더해져
            # 마지막 값으로 출력될 것
            print(answer)
            break