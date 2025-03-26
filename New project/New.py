hoursworked = float(input("How many hours have been worked?: "))
hourlyrate = float(input("What is the hourly rate?: "))
overtime_hours = float(input("Overtime hours: "))
employee_name = input("Enter Employee name: ")

grosspay = hoursworked * hourlyrate
overtime_wage = overtime_hours * 2 * hourlyrate
totalpay = grosspay + overtime_wage

print("")
print(f"Hello {employee_name}")
print(f"Overtime Wage:    {overtime_wage}")
print(f"Gross Wage:       {totalpay}")





# def gross(hoursworked,hourlyrate):
#     z = hoursworked * hourlyrate
#     return z
#print(gross(50,20))