def findNumIn2D(A, N, M, X):
    for i in range(N):
        for j in range(M):
            if A[i][j] == X:
                return True
    return False


N, M = map(int, input().split())
A = []
for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)
X = int(input())

if findNumIn2D(A, N, M, X):
    print("will not take number")
else:
    print("will take number")
