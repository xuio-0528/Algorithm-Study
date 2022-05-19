#######################################################
##
## 백준 24444번 - 알고리즘 수업 - 너비 우선 탐색 1
## acmicpc.net/problem/24444
##
#######################################################

import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    global order

    queue = deque()
    queue.append(R)

    while queue:
        tmp = queue.popleft()
        if visited[tmp] == 0:
            visited[tmp] = order
            order += 1
            for v in edges[tmp]:
                queue.append(v)

N, M, R = map(int, input().split())
edges = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
order = 1

for i in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for i in range(1,N+1):
    edges[i].sort()

bfs()

for i in range(1, N+1):
    print(visited[i])
