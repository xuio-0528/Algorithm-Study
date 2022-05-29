#######################################################
##
## 백준 2331번 - 반복수열
## acmicpc.net/problem/2331
##
#######################################################

A, P = map(int ,input().split())
cache = [A]
k = 0

while(1) :
    tmp = cache[-1]
    val = 0
    while(tmp>0) :
        val += (tmp%10)**P
        tmp //=10
    if val in cache: 
        k = val
        break
    cache.append(val)

print(len(cache[:cache.index(k)]))



