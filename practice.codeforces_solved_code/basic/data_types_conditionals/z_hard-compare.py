import math

A, B, C, D = map(int, input().split())


logA = B * math.log(A)
logC = D * math.log(C)


if logA > logC:
    print("YES")
else:
    print("NO")
