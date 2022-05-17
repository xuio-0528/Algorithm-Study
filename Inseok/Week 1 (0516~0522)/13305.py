#######################################################
##
## 백준 13305번 - 주유소
## acmicpc.net/problem/13305
##
#######################################################

N = int(input())
edge = list(map(int, input().split()))
city = list(map(int, input().split()))
min_price = city[0]
ans = 0

for i in range(N-1):
    if min_price > city[i]:
        min_price = city[i]
    ans += min_price * edge[i]

print(ans)