#Way one
operator = input("Enter a operator (+ - * /): ")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number:"))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"Operator is not valid")

#Way two
expression = input("Enter an expression: ")

result = eval(expression)
print(result)


