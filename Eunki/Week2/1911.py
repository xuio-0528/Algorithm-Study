#######################################################
##
## 백준 1911번 - 흙길 보수하기 - 그리디
## https://www.acmicpc.net/problem/1911
##
#######################################################

import sys
input = sys.stdin.readline

num, length = map(int, input().split())

water_place = [[] for _ in range(num)]

for i in range(num):
    water_place[i] = list(map(int, input().split()))

min_pos = sorted(water_place, key=lambda x: x[0])[0][0]
max_pos = sorted(water_place, key=lambda x: x[1])[::-1][0][1]

water_road = [0 for _ in range(min_pos, max_pos+1)]
for water in water_place:
    for i in range(water[0]-min_pos, water[1]+1 - min_pos):
        water_road[i] = 1

del water_place

cnt = 0
wood = min_pos

for i in range(0, max_pos+1 - min_pos):
    if wood < i and water_road[i] == 1:
        wood = i+length
        cnt+=1

print(cnt)