#######################################################
##
## 백준 1436번 - 분해합 - 브루트 포스
## https://www.acmicpc.net/problem/1436
## N의 숫자를 차감해내려가면서 계속 올라가도록 구현
##
#######################################################

import sys

N = int(input())

start = 666

while True:
    if '666' in str(start):
        N-=1
        if N == 0:
            break
    start +=1

print(start)