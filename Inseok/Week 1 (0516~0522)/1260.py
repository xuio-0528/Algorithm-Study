#######################################################
##
## 백준 1260번 - DFS와 BFS
## acmicpc.net/problem/1260
##
#######################################################

from collections import deque

def dfs(node, visited):
    if node in visited : return
    visited.append(node)

    for v in edges[node]:
        dfs(v, visited)

def bfs(node, visited):
    queue = deque()
    queue.append(node)
    visited.append(node)

    while queue:
        tmp = queue.popleft()
        for v in edges[tmp] :
            if v not in visited :
                visited.append(v)
                queue.append(v)

N, M, V = map(int, input().split())
edges = [[] for _ in range(N+1)]
visited = []

for i in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for i in range(1,N+1):
    edges[i].sort()

dfs(V, visited)
print(*visited)
visited.clear()
bfs(V, visited)
print(*visited)



