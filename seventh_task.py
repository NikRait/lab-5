n = 5 # basic size

# Rectangle
print("rectangle")
for i in range(n):
    print("*" * n)

# Triangle
print("\ntriangle")
for i in range(1, n + 1):
    print("*" * i)

# Spruce
print("\nspruce")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Rhombus
print("\nrhombus")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
