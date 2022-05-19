#######################################################
##
## 백준 1743번 - 음식물 피하기
## acmicpc.net/problem/1743
##
#######################################################

from collections import deque
import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())

sp = [[0 for _ in range(M)] for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0
queue = deque()

for _ in range(K):
    r, c = map(int, input().split())
    sp[r-1][c-1] = 1

for i in range(N):
    for j in range(M):
        tmp = 0
        queue.clear()

        if sp[i][j] == 1:
            sp[i][j] = 2
            tmp += 1
            queue.append((i,j))
            while queue:
                a,b = queue.popleft()
                for k in range(4):
                    cx = a+dx[k]
                    cy = b+dy[k]
                    if 0 <= cx < N and 0 <= cy < M and sp[cx][cy] == 1:
                        queue.append((cx,cy))
                        sp[cx][cy]=2
                        tmp += 1
        ans = max(ans, tmp)

print(ans)
