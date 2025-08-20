print("Please make a choice:")
print("1 is for Park View Condos: $150,000")
print("2 is for Golf Course View Condos: $170,000")
print("3 is for Lake View Condos: $210,000")
answer = int(input("Enter your choice: "))

price = 0
viewname = ""

if answer == 1:
    viewname = "Park View Condo"
    price = 150000
elif answer == 2:
    viewname = "Golf Course View Condo"
    price = 170000
elif answer == 3:
    viewname = "Lake View Condo"
    price = 210000
else:
    print("Invalid condo selection.")

if price > 0:
    print("Choose parking option: ")
    print("1 - Garage for $5,000")
    print("2 - Parking space (free)")

    extra = int(input("Select parking option (1 or 2): "))

    if extra == 1:
        price += 5000
    elif extra == 2:
        print("Its free so no charge.")

    print(f"\nYou selected a {viewname}.")
    print(f"Total price: ${price:,}")
else:
    print("Condo price is $0 due to invalid selection.")

