#task 1

distances = []

for day in range(1, 6):
    d = float(input(f"Day {day}:- Please enter distance travelled:"))
    distances.append(d)

total = sum(distances)
average = total / len(distances)
longest = max(distances)
shortest = min(distances)

print(f"\nTotal distance travelled : {total} kms")
print(f"Average distance travelled : {average} kms")
print(f"Longest distance travelled : {longest} kms")
print(f"Shortest distance travelled: {shortest} kms")

#task2
nums = []

print("Please enter 6 integers:")
for i in range(1, 7):
    val = int(input(f"Enter value {i}: "))
    nums.append(val)

print(f"List after adding integers: {nums}")

index = int(input("Enter the index to update (0-5): "))
while index < 0 or index > 5:
    print("Invalid index. Please enter a number between 0 and 5.")
    index = int(input("Enter the index to update (0-5): "))

new_val = int(input("Enter the new value: "))
nums[index] = new_val

print(f"Updated list: {nums}")

#task3
n = int(input("Number of trainees: "))
averages = []

for t in range(n):
    trainee_num = 4000 + t
    print(f"\nTrainee #{trainee_num}")
    r1 = float(input("Enter Result 1:"))
    r2 = float(input("Enter Result 2:"))
    r3 = float(input("Enter Result 3:"))

    avg = round((r1 + r2 + r3) / 3, 2)
    averages.append(avg)

print("--------------------------------------------------\n")
print("Trainee Statistics")

for i, avg in enumerate(averages):
    trainee_num = 4000 + i
    print(f"Trainee #{trainee_num} Average: {avg}")

overall_avg = round(sum(averages) / len(averages), 2) if averages else 0
max_avg = max(averages) if averages else 0
min_avg = min(averages) if averages else 0
low_count = sum(1 for a in averages if a < 50)

print(f"Average result: {overall_avg}")
print(f"Maximum average: {max_avg}")
print(f"Minimum average: {min_avg}")
print(f"Number of low average results: {low_count}")

