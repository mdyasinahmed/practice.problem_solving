n = int(input())
arr = list(map(int, input().split()))

print(arr[::-1])

print("YES") if arr == arr[::-1] else print("NO") 
