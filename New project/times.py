import time

my_time = int(input("Enter your time: "))

for i in range(0, my_time):
    print(f"Waiting...{i + 1}")
    time.sleep(1)

print(my_time)
print("Done")