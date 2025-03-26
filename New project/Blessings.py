number = int(input("Enter a number: "))
result = number % 2

if result == 1:
    print("Number is odd")
else:
    print("Number is even")


# Program to grade student results:

marks = int(input("Enter your marks: "))

if marks < 0:
    print("Invalid mark")
elif marks >= 75:
    print("dist")
elif marks >= 65:
    print(6)
elif marks >= 60:
    print(5)
elif marks >= 50:
    print(4)
elif marks >= 40:
    print(3)
else:
    print("Failed")
