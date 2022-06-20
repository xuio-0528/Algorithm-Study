#######################################################
##
## 백준 2606번 - 바이러스 - 그래프
## https://www.acmicpc.net/problem/2606
##
#######################################################
from collections import deque
import sys
input = sys.stdin.readline

vertex = int(input())
edge = int(input())
graph = [[] for _ in range(vertex)]
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

queue = deque([0])
visited = [0 for _ in range(vertex)]
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1

print(sum(visited)-1)
            
    