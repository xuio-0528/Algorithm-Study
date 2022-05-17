#######################################################
##
## 백준 11652번 - 카드
## acmicpc.net/problem/11652
##
#######################################################

from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
card = defaultdict(int)

for i in range(N):
    card[int(input())] += 1

max_val = max(card.values())

for key in list(sorted(card.keys())):
    if card[key] == max_val :
        print(key)
        break



