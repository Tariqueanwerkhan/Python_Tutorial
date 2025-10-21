# Argument#s in Functions

# 1. Required Arguments (single/multiple arguments)

# def greetings(name):
#     print("Hello", name, "!")
# greetings("Tarique Anwer Khan")         #Tarique Anwer khan is argument)
# greetings()                   #required an argument to run code


# def intro(course_name, instructor_name):
#     print("Welcome to", course_name, "course by", instructor_name)
# intro("Python", "Tarique Anwer Khan")



# 2. default arguments
# def greetings(name = "World"):                 #"world" is a default value
#     print("Hello", name, "!")
# greetings()
# greetings("Tarique")



# 3. keyword arguments
# def divide(a, b):
#     return a / b
#
# result = divide(a = 100, b = 20)
# print(result)
#
# result = divide(20,100)
# print(result)


# 4. Arbitrary Argument
# Arbitrary Positional Argument (*args)
# Note: stores arguments as tuple

# def add2numbers(a, b):
#     return a + b
# result = add2numbers(10,20)
# print(result)
#
#
# def add3numbers(a, b, c):
#     return a + b + c
# result = add3numbers(10,20,30)
# print(result)
#
#
# def add_numbers(*args):
#     print(type(args))
#     return sum(args)
# op = add_numbers(3, 4, 9, 10)
# print(op)
#
#
# def greetings2(*names):
#     for name in names:
#         print(f"Hello, {name}!")
# greetings2("John", "Smith", "Kristein")



# Arbitrary keyword Argument(**kwargs)
# Note: stores arguments as dictionary

def print_details(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name = "Tarique", age = 24, city = "Delhi")


