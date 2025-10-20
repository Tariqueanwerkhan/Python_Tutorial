# data types in python
a = 1
b = 1
# print(a)
print(a+b)
print(type(a))

c = "1"
d = "1"
print(c+d)    # it will give 11 because of string value
print(type(c))

# basic data type in python
#1 Numeric
a1 = 1          #1a. Integer
a2 = 1.5        #1b. float
print(type(a2))
a3 = complex(3,5)     #1c. complex
print(type(a3))

#2 sequence
b1 = "Tarique"     #2a. string type
print(type(b1))
b2 = [2, 4, 5, 7, 70, "Tarique"]    #2b. list
print(type(b2))
b3 = (2, 4, 5, 7, 70, "Tarique")     #2c. tuple
print(type(b3))

#3 Dictionary
my_dictionary = {'Name': 'John', 'Age': 18, 'city': 'Louisiana'}
print(my_dictionary)
print(type(my_dictionary))

#4 sets
my_sets = {2, 4, 5, 7, 70, "Tarique"}
print(type(my_sets))

#5 Boolean
bool1 = True
bool2 = False
print(type(bool1))

#Binary
# bytes, bytearray,, memoryview
byte1 = b"Traique"
print(type(byte1))