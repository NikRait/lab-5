n = int(input("Enter n: ")) # Getting number from user

a, b = 0,1

print(f"First {n} numbers of Fibonacci series are: ")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Updating values of a and b

print()
