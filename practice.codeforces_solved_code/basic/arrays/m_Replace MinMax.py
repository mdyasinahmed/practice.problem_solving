n = int(input())
arr = list(map(int, input().split()))

mn_in = 0
mx_in = 0

for i in range(1, n):
    if arr[i] < arr[mn_in]:
        mn_in = i
    if arr[i] > arr[mx_in]:
        mx_in = i

arr[mn_in], arr[mx_in] = arr[mx_in], arr[mn_in]

print(*arr)