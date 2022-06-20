#######################################################
##
## 백준 14502번 - 연구소 - 그래프
## https://www.acmicpc.net/problem/14502
##
#######################################################

import queue
import sys
from collections import deque
input = sys.stdin.readline
row, col = map(int, input().split())

lab = []
for i in range(row):
    lab.append(list(map(int, input().split())))

print(lab)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
max_result = 0

def bfs():
    global max_result
    copy = [[0]*col for _ in range(row)]
    virus = []
    for i in range(row):
        for j in range(col):
            copy[i][j] = lab[i][j]
            if copy[i][j] == 2:
                virus.append([i, j])
    result = 0
    queue = deque(virus)
    
                
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and copy[nx][ny] == 0:
                copy[nx][ny] = 2
                queue.append([nx, ny])
    for i in copy:
        for j in i:
            if j == 0:
                result += 1
    max_result = max(max_result, result)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(row):
        for j in range(col):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(cnt+1)
                lab[i][j] = 0
    
wall(0)
print(max_result)
    
    
    