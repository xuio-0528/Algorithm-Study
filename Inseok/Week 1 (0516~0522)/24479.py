#######################################################
##
## 백준 24479번 - 알고리즘 수업 - 깊이 우선 탐색 1
## acmicpc.net/problem/24479
##
#######################################################
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(node, visited):
    global order

    if visited[node] != 0:
        return
    else:
        visited[node] = order
        order += 1

    for v in edges[node]:
        dfs(v, visited)

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

dfs(R, visited)
for i in range(1, N+1):
    print(visited[i])