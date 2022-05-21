#######################################################
##
## 백준 2798번 - 블랙잭 - 브루트 포스
## https://www.acmicpc.net/problem/2798
##
#######################################################


import sys
from itertools import combinations

N, M = map(int,sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))
length = len(num_list)


ans = 0
for num_comb in combinations(num_list, 3):
    temp = sum(num_comb)
    if ans < temp <= M:
        ans = temp

print(ans)
