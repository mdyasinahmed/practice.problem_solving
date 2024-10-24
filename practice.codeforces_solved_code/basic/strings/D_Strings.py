A = input()
B = input()

print(len(A), len(B))
print(A+B)

swapped_A = B[0] + A[1:] if len(A) > 1 else B[0]
swapped_B = A[0] + B[1:] if len(B) > 1 else A[0]

print(swapped_A, swapped_B)