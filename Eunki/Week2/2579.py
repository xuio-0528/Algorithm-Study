#######################################################
##
## 백준 2579번 - 계단 오르기 - DP
## https://www.acmicpc.net/problem/2579
##
#######################################################

import sys
input = sys.stdin.readline

num = int(input())
cost = []
for _ in range(num):
    cost.append(int(input()))

if num == 1:
    print(cost[0])
    
else:
    dp = [0]*(num+1)
    dp[1] = cost[0]
    dp[2] = cost[1] + cost[0]

    for i in range(3, num+1):
        dp[i] = cost[i-1] + max(dp[i-3]+cost[i-2], dp[i-2])

    print(dp[num])