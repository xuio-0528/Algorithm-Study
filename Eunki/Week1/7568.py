#######################################################
##
## 백준 7568번 - 분해합 - 브루트 포스
## https://www.acmicpc.net/problem/2231
## 키와 몸무게를 모두 확인하며 bubble sort로 줄 세운 후에 
## 등수를 매길 때에 뒤에 있는 사람이 나보다 하나라도 크면 동일 등수
## 그리고 그것을 체크해두어 등수가 알맞게 매겨지도록 구현
##
#######################################################

import sys

N = int(sys.stdin.readline())
dung_chi = []
for i in range(N):
    length, weight = map(int, sys.stdin.readline().split())
    dung_chi.append([length, weight])

ans = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if dung_chi[i][0] < dung_chi[j][0] and dung_chi[i][1] < dung_chi[j][1]:
            cnt += 1
    
    ans.append(cnt)
for i in ans:
    print(i, end= " ")
    
    
    


    
    
