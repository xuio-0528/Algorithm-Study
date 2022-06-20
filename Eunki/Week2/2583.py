#######################################################
##
## 백준 2583번 - 영역 구하기 - DFS
## https://www.acmicpc.net/problem/2583
##
#######################################################

import sys
input = sys.stdin.readline

def dfs(y, x, cnt):
    graph[y][x] = 1
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if 0<=ny<m and 0<=nx<n and graph[ny][nx] == 0:
            cnt = dfs(ny, nx, cnt+1)
    return cnt

m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

d = [(0,1), (0,-1), (1,0), (-1,0)]
res = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            res.append(dfs(i, j, 0))

print(len(res))
print(*sorted(res))

