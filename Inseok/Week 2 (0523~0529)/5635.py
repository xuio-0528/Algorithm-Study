#######################################################
##
## 백준 5635번 - 생일
## acmicpc.net/problem/5635
##
#######################################################

N = int(input())
arr=[]
for _ in range(N):
    arr.append(input().split())
arr.sort(key=lambda x : (int(x[3]), int(x[2]), int(x[1])))

print(arr[-1][0])
print(arr[0][0])