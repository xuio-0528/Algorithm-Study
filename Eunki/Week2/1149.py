#######################################################
##
## 백준 1149번 - RGB거리 - DP
## https://www.acmicpc.net/problem/1149
##
#######################################################

import sys
input = sys.stdin.readline

num = int(input())
cost = []
for i in range(num):
    cost.append(list(map(int, input().split())))

dp = [[0]*3 for _ in range(num)]
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]


for i in range(1, num):
    for j in range(3):
        dp[i][j] = cost[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
        
print(min(dp[num-1]))