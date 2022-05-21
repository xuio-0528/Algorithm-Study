#######################################################
##
## 백준 2231번 - 분해합 - 브루트 포스
## https://www.acmicpc.net/problem/2231
## 분해합이 존재하는 모든 숫자를 N까지 구하다가 N이 있는지를 확인
##
#######################################################


import sys

N = int(sys.stdin.readline())

for i in range(1, N):
    temp = sum(map(int, list(str(i))))
    ans = i + temp
    if ans == N:
        print(i)
        break
else:
    print(0)