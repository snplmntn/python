first_name = "Sean"

print(f"Hello {first_name}") # Template Literal

name = input("What is your name: ")

print(f"Hello {name} welcome to our calculator hehe !")
choice = "y"

while(choice != "n"):
    num1 = input("Enter num 1: ")
    operation = input("Enter operation (+, -, *, /): ")
    num2 = input("Enter num 2: ")

    if operation == "+":
        print(f"Result: {int(num1) + int(num2)}")
    elif operation == "-":
        print(f"Result: {int(num1) - int(num2)}")
    elif operation == "*":
        print(f"Result: {int(num1) * int(num2)}")
    elif operation == "/":
        print(f"Result: {int(num1) / int(num2)}")

    choice = input("Would you like to calculate again (y/n): ")

    if choice == "n":
        print("Thank you for using our calculator see you!")
