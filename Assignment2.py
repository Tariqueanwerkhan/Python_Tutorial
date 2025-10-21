# write a python program to input student name and marks of 3 subjects.
# Print name and percentage in output
student_name = input("Enter your name: ")
# input marks from 3 subjects
marks_subject1 = int(input("Enter marks for subject1: "))
marks_subject2 = int(input("Enter marks for subject2: "))
marks_subject3 = int(input("Enter marks for subject3: "))
total_marks = marks_subject1 + marks_subject2 + marks_subject3
percentage = (total_marks / 300) * 100
print(f"\nStudent name: {student_name}\nMarks: {total_marks}\nPercentage: {percentage:.2f}%")


# write a python program that collects multiple types of data(e.g., name, age, height, and student status) from
# user input, stores them in a dictionary, and then prints out the collected data?

# initializing a dictionary

user_data = {}
# input from user
user_data['name'] = input("Enter your name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter your height: "))
user_data['student'] = input("Are you a student (Yes/No): ")
# print the input from user
print(user_data)
