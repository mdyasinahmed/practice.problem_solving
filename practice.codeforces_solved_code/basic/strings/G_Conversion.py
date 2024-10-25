S = input().strip()

S = S.replace(',', ' ')


result = ''.join([char.lower() if char.isupper() else char.upper() for char in S])


print(result)
