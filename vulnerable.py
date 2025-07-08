user_input = input("Enter a Python expression: ")
result = eval(user_input)  # Vulnerable: user input is executed as code
print("Result:", result)
