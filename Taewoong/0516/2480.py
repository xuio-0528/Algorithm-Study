import sys

a, b, c = map(int, sys.stdin.readline().split())

if a == b == c:
  print(10000 + a * 1000)
elif a == b or b == c or c == a:
  if a == b:
    print(1000 + 100 * a)
  elif b == c:
    print(1000 + 100 * b)
  else:
    print(1000 + 100 * c)
else:
  print(max(a,b,c) * 100)
