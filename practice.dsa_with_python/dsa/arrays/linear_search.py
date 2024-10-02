# arr = []
# n = int(input())
# print(n)

# for i in range(n):
#     nums = int(input())
#     arr.append(nums)

# print(arr)
n = int(input())
arr = list(map(int, input().split()))

x = int(input())

if x in arr:
    print("Found")
else:
    print("Not Found")