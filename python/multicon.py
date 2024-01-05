num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1%2==0 and num2 %2==0:
    print("Both are even")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both are odd")
else:
    print("One even, one odd")
