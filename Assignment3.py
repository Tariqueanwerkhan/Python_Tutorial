# write a simple program to determine if a given year is a leap year using user input.
# leap year condition
# divisible by 4 but not divisble by 100
# divisible by 400

# year = int(input("Enter a year (e.g. 2024): "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")



# Q2 Login authentication using conditional statement. assume you have a predefined username and password.
# write a program that prompts the user to enter a username and password and checks whether they match.
# Provide appropriate messages for the following cases:
# Both username and password are correct.
# username is correct but password is incorrect.
# username is correct.
# predefined_username = 'Madhav'
# Predefined_password = 'Pass101'
#
# username = input("Enter your username: ")
# password = input("Enter your password: ")
#
# if username == predefined_username:
#     if password == Predefined_password:
#         print("Welcome! login was  successful.")
#     else:
#         print("Incorrect Password!")
# else:
#     print("Invalid Username!")


# Admission eligibility:
# A university has the following eligibility criteria for admission:
# Marks in Mathematics >= 65.
# Marks in physics >= 55.
# Marks in chemistry >= 50.
# total marks in all three subjects >= 180 or
# total marks in mathematics and physics >= 140
# write a program that takes marks in three subjects as input and
# prints whether the students is eligible for admission.

print("Entr PCM marks out of 100")
physics_marks = int(input("Enter Physics marks: "))
chemistry_marks = int(input("Enter Chemistry marks: "))
mathematics_marks = int(input("Enter Mathematics marks: "))

if(mathematics_marks >= 65 and
    physics_marks >= 55 and
    chemistry_marks >= 50 and
    (mathematics_marks + physics_marks + chemistry_marks) >= 180) or \
    (mathematics_marks + physics_marks) >= 140:
    print("You're eligible!")
else:
    print("Sorry, you're not eligible.")