#task 1

from statistics import mean

rainfall_data = []
for day in range(1, 8):
    value = float(input(f"Day {day} - Please enter rainfall: "))
    rainfall_data.append(value)

average = statistics.mean(rainfall_data)
total = sum(rainfall_data)
print(f"Average: {average:.2f}")
print(f"Total Rainfall is: {total:.2f} mm")

for index, value in enumerate(rainfall_data):
    if value > 3.5:
        print(f"Rainfall exceed 3.5mm on Day : {index + 1}")
 #task2
num = []
for x in range(5):
    number = int(input("Please enter a number: "))
    num.append(number)

print(num)

for v in range(len(num)):
    num[v] = num[v] + 1

print(num)
#task3

names = []
sales = []
num_salespeople = int(input("Enter the number of sales people: "))
for i in range(num_salespeople):
    name = input("Enter name: ")
    amount = float(input("Enter amount: "))
    names.append(name)
    sales.append(amount)
total_sales = sum(sales)
average_sales = mean(sales)
maximum_sales = max(sales)
minimum_sales = min(sales)