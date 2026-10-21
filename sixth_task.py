n = int(input("Enter number: "))
original = n # saving original number
reversed_num = 0

temp = n # temporal n
while temp > 0:
    digit = temp % 10 # getting current last digit
    reversed_num = reversed_num * 10 + digit
    temp //= 10 # removing last digit
    if original == reversed_num:
        print(f"{original} - palindrome")
    else:
        print(f"{original} - not palindrome")

'''
text = input("Enter string: ")
if text == text[::-1]:
    print("Palindrome")
'''
