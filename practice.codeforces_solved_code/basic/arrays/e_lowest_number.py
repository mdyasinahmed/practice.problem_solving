n = int(input())
arr = list(map(int, input().split()))

lowest = min(arr)

pos = arr.index(lowest)

print(lowest, pos)