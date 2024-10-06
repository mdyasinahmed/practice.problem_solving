N, M = map(int, input().split())

res = []

for i in range(N):
    row = list(map(int, input().split()))
    res.append(row)


for row in res:
    print(*row[::-1])
