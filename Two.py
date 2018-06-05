# Kate Williams
# 6/5/2018

fName = input("Please enter your first name: ")
lName = input("Please enter your last name: ")

print("Hello, " + lName + ", " + fName)

num1String = input("Enter first number: ")
num2String = input("Enter second number: ")

num1 = int(num1String)
num2 = int(num2String)

quot = num1 / num2
remain = num1 % num2

print("Quotient is " + str(quot) + " and remainder is " + str(remain))
