# Weight coversion
weight = float(input("Enter your weight: "))
unit = input("What units is it (K / L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid.")

print(f"Your weight is: {weight} {unit}")

number = int(input("Enter your number between 1 - 10: \n"))
print("")
# While loop
while number < 1 or number > 10:
    print(f"Your {number} is not valid.\n")
    number = int(input("Enter your number between 1 - 10: "))

print(f"Your number is {number}")


