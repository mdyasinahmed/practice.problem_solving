
n = int(input())
arr = list(map(int, input().split()))

minimum = min(arr)
# print(minimum)

countMin = arr.count(minimum)
# print(countMin)

if countMin%2 != 0:
    print("Lucky") 
else:
    print("Unlucky") 