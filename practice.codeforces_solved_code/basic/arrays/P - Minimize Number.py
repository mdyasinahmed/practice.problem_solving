def solve(n, arr):
    def countDiv(x):
        count = 0
        while x % 2 == 0:
            x //= 2
            count += 1
        return count

    res = float('inf')
    for num in arr:
        res = min(res, countDiv(num))

    print(res)

n = int(input())
arr = list(map(int, input().split()))
solve(n, arr)
