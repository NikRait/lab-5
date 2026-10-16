n = int(input("Enter n: "))

orig = n # Saving original number

count = 0
total = 0
product = 1
reversed_sum = 0 # Results variables

while n > 0:
    digit = n % 10 # Getting last digit
    count += 1
    total += digit
    product *= digit
    reversed_sum = reversed_sum * 10 + digit # Getting results
    n //= 10 # Removing last digit

print("Number of digits:", count)
print("Sum of digits:", total)
print("Product of digits:", product)
print("Reversed number:", reversed_sum)
