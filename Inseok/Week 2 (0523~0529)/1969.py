#######################################################
##
## 백준 1969번 - DNA
## acmicpc.net/problem/1969
##
#######################################################

N, M = map(int ,input().split())
dna = []
ans_dna = []
ans = 0

for i in range(N):
    dna.append(input())

for i in range(M):
    a = []
    for j in range(N):
        a.append(dna[j][i])
    a.sort()
    ans_dna.append(max(a, key=a.count))
print("".join(ans_dna))

for i in range(N):
    for j in range(M):
        if dna[i][j] != ans_dna[j]:
            ans+=1
print(ans)