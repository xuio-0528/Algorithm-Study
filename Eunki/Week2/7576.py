#######################################################
##
## 백준 2579번 - 토마토 - BFS
## https://www.acmicpc.net/problem/7576
##
#######################################################

import sys
from collections import deque

input = sys.stdin.readline

col, row = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(row)]

start = []
visited = [[0 for _ in range(col)] for _ in range(row)]

for i in range(row):
    for j in range(col):
        if box[i][j] == 1:
            start.append([i, j])
            visited[i][j] = 1

queue = deque(start)
length = len(start)

lr = [0, 0, 1, -1]
ud = [1, -1, 0, 0]


def bfs(queue, box, visited):
    day_cnt = -1
    temp_length = len(queue)
    zero_check = 0
    for i in range(len(box)):
        for j in range(len(box[0])):
            if box[i][j] == 0:
                zero_check = 1
    if zero_check == 0:
        return 0

    while temp_length > 0:            
        x, y = queue.popleft()
        for i in range(4):
            nx = x + lr[i]
            ny = y + ud[i]
            if 0 <= nx < row and 0 <= ny < col:
                if box[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    box[nx][ny] = 1
        temp_length -= 1
        
        if temp_length == 0:
            day_cnt += 1
            temp_length = len(queue)
    zero_check = 0
    for i in range(len(box)):
        for j in range(len(box[0])):
            if box[i][j] == 0:
                zero_check = 1
    if zero_check == 1:
        return -1
        
    return day_cnt

print(bfs(queue, box, visited))