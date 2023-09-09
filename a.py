#write a code for a calculator
#addition
#subtraction
#multiplication
#division
#modulus
#exponent
#floor division
#take input from the user
#take input for the operation
#perform the operation

#take input from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
#take input for the operation
operation = input("Enter the operation: ")

#perform the operation
if operation == "+":
    print("The sum of the two numbers is: ", int(num1) + int(num2))
elif operation == "-":
    print("The difference of the two numbers is: ", int(num1) - int(num2))
elif operation == "*":
    print("The product of the two numbers is: ", int(num1) * int(num2))
elif operation == "/":
    print("The quotient of the two numbers is: ", int(num1) / int(num2))
elif operation == "%":
    print("The modulus of the two numbers is: ", int(num1) % int(num2))
elif operation == "**":
    print("The exponent of the two numbers is: ", int(num1) ** int(num2))
elif operation == "//":
    print("The floor division of the two numbers is: ", int(num1) // int(num2))
else:
    print("Invalid operation")
    