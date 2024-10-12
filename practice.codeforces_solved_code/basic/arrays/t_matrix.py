n = int(input())

sum_1 = 0
sum_2 = 0

for i in range(n):
    row = list(map(int, input().split()))
    
    sum_1 += row[i]
    
    sum_2 += row[n-i-1]

print(abs(sum_1 - sum_2))
