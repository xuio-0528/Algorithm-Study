#######################################################
##
## 백준 1946번 - 신입 사원 - Greedy
## https://www.acmicpc.net/problem/1496
##
#######################################################

import sys
input = sys.stdin.readline

test_case = int(input())
answer_list = []
for _ in range(test_case):
    num = int(input())
    score = [[] for _ in range(num)]
    for i in range(num):
        score[i] = list(map(int, input().split()))
    score.sort()
    answer = 1
    max_score = score[0][1]
    for i in range(1, num):
        if max_score > score[i][1]:
            answer += 1
            max_score = score[i][1]
    
    answer_list.append(answer)

for i in answer_list:
    print(i)
                