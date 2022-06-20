#######################################################
##
## 백준 9663번 - n-queen - 백트레킹
## https://www.acmicpc.net/problem/9663
##
#######################################################
from collections import deque

n = int(input())

row = []
col = []

row = [0] * n

ans = 0

def n_queen(cnt):
    global ans
    if cnt == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[cnt] = i
            if check(cnt):
                n_queen(cnt + 1)

def check(cnt):
    for i in range(cnt):
        if row[i] == row[cnt] or abs(row[i] - row[cnt]) == cnt - i:
            return False
    
    return True

n_queen(0)
print(ans)
    