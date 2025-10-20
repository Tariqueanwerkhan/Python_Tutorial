# input function in python

# a = input()
# print(int(a)+int(a))
# input function always reads input value as a string

# name = input("Enter your name: ")
# print(f"welcome {name} to the python tutorial series")

# age = input("Enter your age: ")
# print(f"ooh you're just {age} years old!")
# print(f"So next year you will be {int(age)+1}!")


# multiple input from user
# input from uer to add two numbers and print result

# x = input("Enter first number: ")
# y = input("Enter second number: ")
# print(f"summ of {x} and {y} is {int(x)+int(y)}")

student_name = input("Enter your name: ")
# input marks from 3 subjects
marks_subject1 = int(input("Enter marks for subject1: "))
marks_subject2 = int(input("Enter marks for subject2: "))
marks_subject3 = int(input("Enter marks for subject3: "))
total_marks = marks_subject1 + marks_subject2 + marks_subject3
percentage = (total_marks / 300) * 100
print(f"\nStudent name: {student_name}\nMarks: {total_marks}\nPercentage: {percentage:.2f}%")


