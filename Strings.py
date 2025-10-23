# Strings in Python - PART 1
# strings- chars in single, double and triple quotes

# name = "Madhav"     # creating a string
# print(name)
#
# print(type(name))   # checking data type
#
# print("It's easy")
# print("Hello World")
#
# print(''' "kw-double Quotes" ''')
# print(" \"kw-double Quotes\" ")



# 1. old style formatting - % operator

# name = "Madhav"
# age = 16
# print("My name is %s and I'm %d" % (name, age))
# %s, %d are placeholders for the string and int



#2. str.format() method

# name = "Tarique"
# age = 24
# print("My name is {} and I'm {}.". format(name, age))
# # you can also reference the variables by index or keyword.
# print("My name is {0} and I'm {1}.".format(name, age))
#
# print("My name is {name} and I'm {age}.".format(name = "Charlie", age = 24))


# 3. f-strings
# name = "Tarique"
# age = 24
# print(f"My name is {name} and I'm {age}.")
# # you can also perform expressions inside the placeholders.
# print(f"In 5 years, I will by {age + 5} yeard old.")


# Escape Characters - backslash with chars
# print(''' "kw-double Quotes" ''')
# print(" \"kw-double Quotes\" ")           #double quotes using
# print(" \'kw-single Quotes\' ")           #single quotes using
#
# print("Hello\nWorld")
# print("Hello\tWorld")


# String Operators in Python
# a = "Hello"
# b = "Python"
#
# print(a + b)            #concatenate
# print(a*2)

# []- slice, [:]- range


# if "H" in a:
#     print("Yes")
# else:
#     print("No")
#
#
# if "p " not in a:
#     print("Yes")
# else:
#     print("No")
#
# print(r"Hello\nWorld")      # suppress the escape chars


#  string indexing
# my_name = "Tarique"
# print(my_name[0])
# print(my_name[1])
# print(my_name[2])
# print(my_name[3])
# print(my_name[4])
# print(my_name[5])
# print(my_name[6])
# print(my_name[-1])
#
# name2 = "Hello World"
#
# print(name2[5])
# print(name2[-1])
# print(name2[-3])
# print(name2[-4])
#
#
# # string slicing
# my_name = "Tarique Anwer Khan"
# print(my_name[0:3])
# print(my_name[-3:])
# print(my_name[0:3:1])
#
# print(my_name[3:10:1])
# print(my_name[0:5:2])
# print(my_name[0:8:3])
# print(my_name[0:5:4])
# print(my_name[0:9])        # first 2 chars
# print(my_name[0:3])        # first 3 chars
# print(my_name[2:5])        # third to fifth chars
# print(my_name[1:4])        # second to fourth chars
# print(my_name[-1:])        # last char of str
# print(my_name[5:])         # last char of str
# print(my_name[-2:])        # last 2 char of str
# print(my_name[-3:])        # last 3 char of str
# print(my_name[0::2])       # every second char
# print(my_name[:])          # all char
# print(my_name[::])         # all char
# print(my_name[::-1])       # reverse the string



# string methods
word = "Hello, Tarique"
#1. len()
print(len(word))

#2. upper()
print(word.upper())

#3. lower()
print(word.lower())

#4. count()
print(word.count('T'))

#5. find()
print(word.find('r'))

#6. split()
print(word.split(','))
print(word.split())

# 7.replace()
print(word.replace("Tarique", "Anwer"))

#8. title()
print(word.title())

#9. strip()
word2 = "    Hello World    "
print(len(word2))
print(word2.strip())

#10. join()
zwords = ("Tarique", "is", "Great")
print(" ".join(zwords))
print("-".join(zwords))





