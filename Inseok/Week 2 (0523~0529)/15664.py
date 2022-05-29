#######################################################
##
## 백준 15664번 - N과 M(10)
## acmicpc.net/problem/15664
##
#######################################################

def dfs(l, visited):
    global ans
    if len(l)==M+1:
        if l[1:] in ans:
            return
        else :
            ans.append(l[1:])
            return print(*l[1:])
    
    for i in range(N):
        if i not in visited and l[-1]<=arr[i]:
            l.append(arr[i])
            visited.append(i)
            dfs(l, visited)
            l.pop(-1)
            visited.pop(-1)

N, M = list(map(int, input().split()))
arr = list(map(int ,input().split()))
ans = []
arr.sort()

dfs([0], [])