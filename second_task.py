n = int(input("Enter n: ")) # Getting n from user

sum_n = 0
product = 1
sum_squares = 0

for i in range(1, n + 1):
    sum_n += i # Sum of numbers from 1 to n
    product *= i # Product of numbers from 1 to n
    sum_squares += i ** 2 # Sum of squares of numbers from 1 to n

print(f"Sum: {sum_n}")
print(f"Product: {product}")
print(f"Sum of squares: {sum_squares}") # Printing the results
