##################
# 아이디어 : B의 대수와 반대로 A를 정렬하면 S도 가장 작게 나오지 않을까
##################

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

index_list = [x for x in range(n)]

c = zip(index_list, b)
index_list = [x for x, _ in sorted(c, key= lambda x: x[1], reverse=True)]


a.sort()
d = zip(index_list, a)
a = [x for _, x in sorted(d, key= lambda x: x[0])]

calc_list = zip(a, b)

ans = 0
for a, b in calc_list:
    ans += (a * b)

print(ans)