A, B, C, D = map(int, input().strip().split())


product = 1

product = (product * (A % 100)) % 100
product = (product * (B % 100)) % 100
product = (product * (C % 100)) % 100
product = (product * (D % 100)) % 100


print(product)
