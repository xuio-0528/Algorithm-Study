#######################################################
##
## 백준 3986번 - 좋은 단어
## acmicpc.net/problem/3986
##
#######################################################

N = int(input())
cnt = 0

for _ in range(N):
    a = input()
    stack = []
    for chr in a:
        if len(stack) == 0: stack.append(chr)
        else :
            if stack[-1] == chr : stack.pop(-1)
            else : stack.append(chr)
    if len(stack) == 0 : cnt += 1

print(cnt)
        