#######################################################
##
## 백준 1449번 - 수리공 항승
##
#######################################################

N, L = map(int, input().split())
hole = list(map(int, input().split()))

hole.sort()
tmp = 0
ans = 0
tmp_idx = 0

for i in range(1,N):
    diff = hole[i]-hole[i-1]
    tmp += diff
    if tmp >= L:
        ans += 1
        tmp = 0
        if i == N-1:
            ans+=1

if tmp>0 : ans+=1
if N == 1 : ans = 1
print(ans)
