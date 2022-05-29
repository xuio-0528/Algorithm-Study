#######################################################
##
## 백준 2004번 - 조합 0의 개수
## acmicpc.net/problem/2004
##
#######################################################

def foo(k, p):
    cnt = 0
    while k>=p:
        cnt += k//p
        k //= p
    return cnt

N, M = list(map(int, input().split()))

print(min(foo(N,2)-foo(M,2)-foo(N-M,2), foo(N,5)-foo(M,5)-foo(N-M,5)))