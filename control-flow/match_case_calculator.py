num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
d_type = input("Choose the operation (+, -, *, /): ")

match d_type:
    case "+":
        print(f"The result is {num1 + num2}.")
    case "-":
        print(f"The result is {num1 - num2}.")
    case "*":
        print(f"The result is {num1 * num2}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {num1 / num2}.")
    case _:
        print("You have the wrong operation.")
