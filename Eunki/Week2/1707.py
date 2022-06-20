#######################################################
##
## 백준 1707번 - 토마토 - BFS
## https://www.acmicpc.net/problem/1707
## https://ji-gwang.tistory.com/293
##
#######################################################
from collections import deque
import queue
import sys
input = sys.stdin.readline

test_case = int(input())


answer_list = []

for test in range(test_case):
    vertex, edge = map(int, input().split())
    if edge == 0:
        answer_list.append("YES")
        continue
    edge_list = []
    start_list = [[] for _ in range(vertex+1)]
    color = [0] * (vertex+1)
    # 색은 1과 2로 칠할 것
    for _ in range(edge):
        edge_list.append(list(map(int, input().split())))
    
    for i in range(edge):
        start_list[edge_list[i][0]].append(edge_list[i][1])
        start_list[edge_list[i][1]].append(edge_list[i][0])
    start = edge_list[0][0]
    color[start] = 1
    queue = deque([start])
    
    check = 0
    
    while queue:
        x = queue.popleft()
        for i in range(len(start_list[x])):
            # if edge_list[i][0] == x:
            if color[start_list[x][i]] == color[x]:
                check = 1
                break
            if color[x] == 1 and color[start_list[x][i]] == 0:
                color[start_list[x][i]] = 2
            elif color[x] == 2 and color[start_list[x][i]] == 0:
                color[start_list[x][i]] = 1 
            else:
                continue
            if check != 1:              
                queue.append(start_list[x][i])
        if check ==1:
            break
    # if check == 1:
    #     break
    if check == 1:
        answer_list.append("NO")
    else:
        answer_list.append("YES")

for i in range(len(answer_list)):
    print(answer_list[i])