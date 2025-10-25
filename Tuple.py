# Tuples in python
from operator import index

# my_tuple = (1, 2, 3, 4, 5, 6)
# print(my_tuple)
# print(type(my_tuple))
#
#
# # create tuples
# # using parenthesis
# my_tuple1 = (1, "Alpha", True, 3.14)
# print(my_tuple1)
#
# # without parenthesis
# tuple2 = 1,2,3,4,5,6
# print(tuple2)
# print(type(tuple2))
#
#
# # tuple constructor
# tuple2 = tuple((1, 2, 3, 4, 5, 6))
# print(type(tuple2))
# print(tuple2)
#
#
# list1 = [1,2,3,4,5,6]
# new_tuple = tuple(list1)
# print(new_tuple)
#
#
# # create a single element
# # a = ("a")    # it is string
# a = ("a",)    # it will become tuple by adding comma
# print(type(a))
#
#
# # access tuple - indexing
# fruits = ("apple", "banana", "cherry", "orange", "strawberry", "watermelon")
# print(fruits[0])
# print(fruits[-1])
# print(fruits[-2:])
# print(fruits[:3])
# print(fruits[::-1])
# print(fruits[1:4])
#
# # tuple slicing
# new_tuple = (30, 20, 40, 60, 10, 90, 50)
# print(new_tuple)
# print(new_tuple[1:3])
# print(new_tuple[-2:])
# print(new_tuple[0::2])
# print(new_tuple[::-1])
# print(new_tuple[3:])


# tuple operations
# concatenate - join tuples
# tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# tuple2 = ('a', 'b', 'c', 'd', 'e')
#
# tuple3 = tuple1 + tuple2
# print(tuple3)
#
#
# # repetitive
# tuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) * 3
# print(tuple2)
#
# # checking an element in a tuple
# tuple12 = (11, 21, 13, 42, 45, 16, 57, 68, 91, 10)
# print(11 in tuple12)
# print(13 in tuple12)
# print(17 in tuple12)
# print(22 in tuple12)
# print(68 in tuple12)


# # tuple iteration
# # for loop
# fruits = ("apple", "banana", "cherry", "orange", "strawberry", "watermelon")
# for i in fruits:
#     print(i)

# while loop
# fruits = ("apple", "banana", "cherry", "orange", "strawberry", "watermelon")
# i = 0
# print(len(fruits))
# while i < len(fruits):
#     print(fruits[i])
#     i += 1



# # tuple method
# color = ("red", "green", "blue", "black", "white", "yellow", "green", "white")
# # count
# print(color.count("green"))
# print(color.count("black"))
# print(color.count("white"))
# print(color.count("red"))
#
# # index
# print(color.index("green"))


# tuple functions
# numbers = (3, 1, 4, 10, 9, 6, 8)
# # len
# print(len(numbers))
# # sum
# print(sum(numbers))
# # min
# print(min(numbers))
# # max
# print(max(numbers))


# # sort
# numbers = (3, 1, 4, 10, 9, 6, 8)
# a = sorted(numbers)    # tuple is now list
# numbers_sorted = tuple(a)
# print(numbers_sorted)
# # print(type(numbers_sorted))



# # tuple pack and unpack
# a = "charles"
# b = 23
# c = "data scientist"
# tuple_pack = a,b,c
# print(tuple_pack)
#
# name, age, profession = tuple_pack
# print("Name is", name)
# print("age is", age, "years old")
# print("and he is", profession)


# # tupple modification
# tuple_numbers = (10, 20, 30, 40, 50, 60, 70)
# # mutate/modify tuple
# list_numbers = list(tuple_numbers)
# print(list_numbers)
#
# tuple_numbers = tuple(list_numbers)
# print(tuple_numbers)

