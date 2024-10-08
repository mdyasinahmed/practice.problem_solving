N, Q = map(int, input().split())
A = set(map(int, input().split())) 


for _ in range(Q):
    X = int(input())
    if X in A:
        print("found")
    else:
        print("not found")
