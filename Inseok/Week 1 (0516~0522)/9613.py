#######################################################
##
## 백준 9613번 - GCD 합
## acmicpc.net/problem/9613
##
#######################################################

import math
from itertools import combinations

T = int(input())

for i in range(T):
    ans = 0
    num = list(map(int, input().split()))
    for (a,b) in list(combinations(num[1:], 2)):
        tmp = math.gcd(a,b)
        ans+=tmp

    print(ans)