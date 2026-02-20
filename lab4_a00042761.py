from statistics import mean

hourly_rate_of_employees = [
    [10.5, 12.0, 14.5, 16.75, 18.0],
    [20.5, 22.25, 24.0, 26.25, 28.0],
    [34.0, 36.5, 38.0, 40.35, 43.0],
    [50.0, 60.0, 70.0, 80.0, 99.99]
]

print("STEP 1", "STEP 2", "STEP 3", "STEP 4", "STEP 5")
print("---------------------------------------------")
for i, row in enumerate(hourly_rate_of_employees):
        grade_one = row[0]
        grade_two = row[1]
        grade_three = row[2]
        grade_four = row[3]
        grade_five = row[4]
        print(f'Grade : {i + 1} {grade_one:<7}{grade_two:<7}{grade_three:<7}{grade_four:<7}{grade_five:<7}')

for i, row in enumerate(hourly_rate_of_employees):
    if i == 2:
        average = mean(row)
        print(f"Average hourly rate for Grade {i + 1}: {average:.2f}")

for i, row in enumerate(hourly_rate_of_employees):
    average_every_row = mean(row)
    print(f"Average hourly rate for Grade {i + 1}: {average_every_row:.2f}")
difference = None
for i, row in enumerate(hourly_rate_of_employees):
        lowest = min(row)
        highest = max(row)
        difference = highest - lowest
        print(f"Difference between highest and lowest hourly rate for Grade {i + 1}: {difference:.2f}")
print("-" * 60)
print(" " * 20 + "Payscale Table")
print("-" * 60)

print(f"{'':11} {'Step 1':>7} {'Step 2':>7} {'Step 3':>7} {'Step 4':>7} {'Step 5':>7}")
print("-" * 60)


for i, row in enumerate(hourly_rate_of_employees):
    for j in range(len(row)):
        hourly_rate_of_employees[i][j] += 1.5

for i, row in enumerate(hourly_rate_of_employees):
        grade_one = row[0]
        grade_two = row[1]
        grade_three = row[2]
        grade_four = row[3]
        grade_five = row[4]
        line = f"Grade : {i:<2}"
        for value in row:
            line += f"{value:8.2f}"

        print(line)
