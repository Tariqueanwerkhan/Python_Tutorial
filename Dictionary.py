# Dictionary in Python

# syntax:
# my_dict = {'key1' : 'value1', 'key2' : 'value2', ...}


# methods to create dictionary

# method-1 create dictionary using curly braces
cohort = {'course' : 'Python',
          'Instructor' : 'Tarique Anwer Khan',
          'Level1': 'Beginners'}
print(cohort)
print(type(cohort))


# Method-2 using dict() constructor
person = dict(name = 'Tarique Anwer Khan', age = 25, grade = 'A')
print(person)
print(type(person))


# Method-3 using list of tuples
person2 = dict([('name', 'Tarique Anwer Khan'), ('age', 25), ('city', 'New Delhi')])
print(person2)
print(type(person2))



# access dictionary values
student = {
    1: 'Class-X',
    'name': 'Tarique',
    'grade': 'A',
    'city': 'New Delhi'
}
print(student)
print(type(student))

print(student['name'])
print(student['grade'])



# Dictionary methods
student = {
    1: 'Class-X',
    'name': 'Taique Anwer Khan',
    'grade': 'A',
    'city': 'New Delhi'
}

# keys
print(student.keys())
# values
print(student.values())
# items
print(student.items())
# get
print(student['name'])
print(student.get('email', 'Not Present'))


# Add or modify items in dictionary
student = {
    'name': 'Rahul',
    'grade': 'A',
    'city': 'New Delhi'
}
# add item - assign operator
student['email'] = 'Rahul0123@gmail.com'
print(student)

# modify or replace item - assign operator
student ['grade'] = 'A+'
print(student)

# remove items
# delete to remove items
del student['grade']
print(student)

# pop method
var1 = student.pop('email')
print(var1)
print(student)



# dictionary iteation
student = {
    'name': 'Rahul',
    'grade': 'A',
    'city': 'New Delhi'
}
# loop through keys
for keys in student:
    print(keys)

# loop through values
for values in student:
    print(student[values])

# using .values() method
for value in student.values():
    print(value)

# loop through both key-value pair
for keys, value in student.items():
    print(keys, value)



# Nested Dictionary
main_student = {
    'student1' : {'name': 'Rohit', 'age': 23},
    'student2' : {'name': 'Rahul', 'age': 26, 'grade': 'A'}
}
print(main_student)


# Access value
print(main_student['student1'])

print(main_student['student1']['name'])
print(main_student['student2']['grade'])



# Dictionary comprehension

# syntax
# new_dict =
# {key_exp : value_exp for item in iterable if condition}

my_dict = {x: x*x for x in range(1,11)}
print(my_dict)
