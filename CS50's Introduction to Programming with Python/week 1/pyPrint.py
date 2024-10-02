#python print function

# print(*objects, sep=' ', end='\n', file=None, flush=False)
"""
name = input("Your name: ")

print("hello, ", end="")
print(name)
"""
"""
for i in range(0,5):
    print(i, i*i, sep=" ", end=" ")
"""
"""
name = input("Your name: ")

# remove whitespace from str
name = name.strip()

# capitalize user's name
name = name.capitalize()

# title based capitalization
name = name.title()
"""


# reduce code
#name = name.strip().title()

name = input("Your name: ").strip().title()

print(f"hello, {name}")

