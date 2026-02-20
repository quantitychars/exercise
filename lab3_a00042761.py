#task 1
# fitness = [
#     [5400, 6200],
#     [8250, 7900],
#     [4600, 5020]
# ]
# print("Participants","Week 1", "Week 2")
# print("-------------------------------")
# for i, row in enumerate(fitness):
#     Week_one = row[0]
#     Week_two = row[1]
#
#     print(f'{i+1} {Week_one:<7}{Week_two:<7}')

#task2
# steps_data = [
#     [5400, 6200],
#     [8250, 7900],
#     [4600, 5020]
# ]
# week_one_steps = int(input("Please enter your  steps for week one: "))
# week_two_steps = int(input("Please enter your steps  for week two: "))
# new_participant = [week_one_steps, week_two_steps]
# steps_data.append(new_participant)
# print("Participants","Week 1", "Week 2")
# print("-------------------------------")
# for i, row in enumerate(steps_data):
#     Week_one = row[0]
#     Week_two = row[1]
#
#     print(f'{i+1} {Week_one:<7}{Week_two:<7}')

#task3
# steps_data = [
#     [5400, 6200],
#     [8250, 7900],
#     [4600, 5020]
# ]
# week_one_steps = int(input("Please enter your  steps for week one: "))
# week_two_steps = int(input("Please enter your steps  for week two: "))
# new_participant = [week_one_steps, week_two_steps]
# steps_data.append(new_participant)
# print("Participants","Week 1", "Week 2", "Improvements")
# print("-------------------------------")
# for i, row in enumerate(steps_data):
#     week_one = row[0]
#     week_two = row[1]
#     improvements = week_two - week_one
#
#     print(f'{i+1} {week_one:<7}{week_two:<7}{improvements:<7}')
#task 4
#version a
# steps_data = [
#     [5400, 6200],
#     [8250, 7900],
#     [4600, 5020]
# ]
# week_one_steps = int(input("Please enter your  steps for week one: "))
# week_two_steps = int(input("Please enter your steps  for week two: "))
# new_participant = [week_one_steps, week_two_steps]
# steps_data.append(new_participant)
# print("Participants","Week 1", "Week 2", "Improvements")
# print("-------------------------------")
# max_impr = None
# min_impr = None
# max_index = None
# min_index = None
# for i, row in enumerate(steps_data):
#     week_one = row[0]
#     week_two = row[1]
#     improvements = week_two - week_one
#     print(f'{i+1} {week_one:<7}{week_two:<7}{improvements:<7}')
#
#     if max_impr is None or improvements > max_impr:
#         max_impr = improvements
#         max_index = i
#
#     if min_impr is None or improvements < min_impr:
#         min_impr = improvements
#         min_index = i
#
# print(f"Participant {max_index+1} got max improvements: {max_impr}")
# print(f"Participant {min_index+1} got min improvements: {min_impr}")
# version b
# steps_data = [
#     [5400, 6200],
#     [8250, 7900],
#     [4600, 5020]
# ]
# week_one_steps = int(input("Please enter your  steps for week one: "))
# week_two_steps = int(input("Please enter your steps  for week two: "))
# new_participant = [week_one_steps, week_two_steps]
# steps_data.append(new_participant)
# print("Participants","Week 1", "Week 2", "Improvements")
# print("-------------------------------")
#
# for i, row in enumerate(steps_data):
#     week_one = row[0]
#     week_two = row[1]
#     improvements = week_two - week_one
#
#     print(f'{i+1} {week_one:<7}{week_two:<7}{improvements:<7}')
#
# improvements = [row[1]-row[0] for row in steps_data]
# max_impr = max(improvements)
# min_impr = min(improvements)
# max_index = improvements.index(max_impr) +1
# min_index = improvements.index(min_impr) +1
#
# print(f"Participant {max_impr} improvement: {max_impr}")
# print(f"Participant {min_impr} improvement: {min_impr}")
#task5
steps_data = [
    [5400, 6200],
    [8250, 7900],
    [4600, 5020]
]
week_one_steps = int(input("Please enter your  steps for week one: "))
week_two_steps = int(input("Please enter your steps  for week two: "))
new_participant = [week_one_steps, week_two_steps]
steps_data.append(new_participant)
print("Participants","Week 1", "Week 2", "Improvements", "Status")
print("--------------------------------------------------------")
for i, row in enumerate(steps_data):
    week_one = row[0]
    week_two = row[1]
    improvements = week_two - week_one
    if 10000<= week_two:
        status = "Met Goal"
    else:
        status = "Below Goal"
    print(f'{i+1} {week_one:<7}{week_two:<7}{improvements:<7}{status:<7}')
