# def double_list(numbers):
#     dubled_nums_list = []
#     for x in numbers:
#         dubled_nums_list.append(x*x)

#     return dubled_nums_list

# result = double_list(numbers = [2, 4, 6, 8])
# print(result)

# students = {
#     "Aman": 80,
#     "Riya": 95,
#     "Rahul": 65
# }

# def highest_marks(students):
#     highest = None
#     for x in students:
#         if highest == None or x > highest:
#             highest = x
#     return highest

# result = highest_marks(students)

# print(result)

students = [("Aman", 80), ("Riya", 95), ("Rahul", 65)]

shorted_marks = sorted(students, key=lambda x: x[1])

print(shorted_marks)