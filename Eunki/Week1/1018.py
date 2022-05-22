#######################################################
##
## 백준 1018번 - 체스판 - 브루트 포스
## https://www.acmicpc.net/problem/1018
## 4중 for문 외에는 별 방벅이 생각나지 않는다.
## 대신 효율적으로 하기 위해 짝수 홀수를 나눠서 하는 방식
##
#######################################################

import sys

row, col = map(int,sys.stdin.readline().split())
chess = []
for i in range(row):
    chess.append(sys.stdin.readline()[:-1])
ans = []
for row_num in range(row-7):
    for col_num in range(col-7):
        cnt_left = 0
        cnt_right = 0
        # 두가지 경로가 있을 것 첫 시작이 B
        for i in range(row_num, row_num+8):
            for j in range(col_num, col_num+8):
        
                if ((i%2==0) and (j%2==0)) or ((i%2==1) and (j%2==1)):
                    if chess[i][j] == 'B':
                        cnt_left += 1
                
                elif ((i%2==0) and (j%2==1)) or ((i%2==1) and (j%2==0)):
                    if chess[i][j] == 'W':
                        cnt_left += 1
        # 시작이 W
        for i in range(row_num, row_num+8):
            for j in range(col_num, col_num+8):
                if ((i%2==0) and (j%2==0)) or ((i%2==1) and (j%2==1)):
                    if chess[i][j] == 'W':
                        cnt_right += 1
                
                elif ((i%2==0) and (j%2==1)) or ((i%2==1) and (j%2==0)):
                    if chess[i][j] == 'B':
                        cnt_right += 1
        
        temp = min(cnt_left, cnt_right)
        ans.append(temp)
            
        
print(min(ans))
        
        
