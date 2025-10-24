# Lists in Python
# create list

# my_list = [1,2,3,4,5]
# print(my_list)

# print(type(my_list))

# my_list2 = [1, 'Indonesia', 'Singapore', True, 3.14]
# print(my_list2)
# print(type(my_list2))

# my_list3 = [1,2, [4,6], True, False, [7,8,9]]
# print(my_list3)
# print(type(my_list3))


# Access list - Indexing
# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
# print(list1[0])
# print(list1[1])
# print(list1[5])
# print(list1[-1])
# print(list1[-2])
# print(list1[-3])
# print(list1[-7])

# list - slicing
# list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# # slicing syntax
# # list_name[start:stop:step]
#
# print(list2)
# print(list2[:3])
# print(list2[0:3:1])
# print(list2[1:5])
# print(list2[-8:-2])
# print(list2[-4:])
# print(list2[-2:])
# print(list2[::1])
# print(list2[::3])
# print(list2[::-1])


# # list modify
# my_list = ['apple', 'guava', 'watermelon', 'raspberry', 'avocado']
# print(my_list)
#
# # replace element at index 1
# my_list[1] = "lichi"
# print(my_list)
#
# # add element in list
# my_list.append("pineapple")
# print(my_list)
#
# #remove element from the list
# my_list.remove("lichi")
# print(my_list)
#
# # list method..........
#
# # 1 append
# fruits = ['watermelon', 'raspberry', 'avocado']
# fruits.append('mango')
# print(fruits)
#
# # extend
# fruits = ['watermelon', 'raspberry', 'avocado']
# more_fruits = ['mango', 'apple']
# fruits.extend(more_fruits)
# print(fruits)
#
# # insert
# fruits = ["watermelon", "raspberry", "avocado"]
# fruits.insert(1, "Orange")
# print(fruits)
#
# # remove
# fruits = ["watermelon", "orange", "raspberry", "avocado"]
# fruits.remove("watermelon")
# print(fruits)
#
# # clear
# fruits = ["watermelon", "raspberry", "avocado"]
# fruits.clear()
# print(fruits)
#
# # finding index
# fruits = ["apple", "avocado", "watermelon", "raspberry", "avocado"]
# index = fruits.index("avocado")
# print(index)
#
# # finding index - within a range
# index = fruits.index("avocado",2)
# print(index)
#
# # count elements
# fruits = ["avocado", "watermelon", "raspberry", "avocado"]
# count = fruits.count("avocado")
# print(count)
#
# # reverse list
# fruits = ["watermelon", "raspberry", "avocado"]
# fruits.reverse()
# print(fruits)
#
# # sorting list
# numbers = [40, 30, 70, 20, 90, 50, 10]
# numbers.sort()  # default sort ascending order
# print(numbers)
#
# # sorting list in descending order
# numbers.sort(reverse=True)
# print(numbers)
#
# # sorting string in a list
# fruits = ["watermelon", "raspberry", "avocado", "orange"]
# fruits.sort()
# print(fruits)
#
# # sorting with a key
# fruits.sort(key = len, reverse = True)
# print(fruits)
#
# # 10 pop with index value
# numbers = [40, 30, 70, 20, 90, 50, 10]
# popped = numbers.pop(4)
# print(popped)   # output: popped 4th index value 90
# print(numbers)
#
# # pop with default
# last = numbers.pop()
# print(last)       # output: pop last value by default 10
# print(numbers)
#
#
# # copying list
# fruits = ["watermelon", "raspberry", "avocado"]
# copy_fruits = fruits.copy()
# print(copy_fruits)
#
# # copying list: modifying the copy does ot affect the original list
# copy_fruits.append("orange")
# print(copy_fruits)
# print(fruits)



# join list
# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# # using + operator
# final_list = list1 + list2
# print(final_list)


# using append method
# for x in list2:
#     list1.append(x)
# print(list1)

# using extend method
# list1.extend(list2)
# print(list1)



# list comprehension
# syntax:
# list_name = [expressions for item in iterable if condition]

# 3 main components of list comprehension
# expression, for clasue, if condition

# create a list of square
# square = [x**2 for x in range(1,6)]
# print(squares)
#
# # filter even numbers
# even_list = [x for x in range(1,20) if x % 2 == 0]
# print(even_list)
#
# # apply function to each element of a list
# my_list = ['apple', 'banana', 'cherry']
# # my_name = "Kishore kumar"
# # print(my_name)
# # print(my_name.upper())
# print(my_list)
# # print(my_list.upper()) # wrong way
# uppercase_list = [lst.upper() for lst in my_list]
# print(uppercase_list)
#
#
# # flatten a nested list using list comprehension
# nested_list = [[1,2], [3,4], [5,6], [7,8]]
# result = [item for sublist in nested_list for item in sublist]
# print(result)
#
# def flatten_list(lst):
#     return [item for sublist in lst for item in sublist]
# final_list = flatten_list(nested_list)
# print(final_list)




# list iteration

# fruits = ['apple', 'banana', 'cherry']
# # using for loop
# for fruit in fruits:
#     print(fruit)
# print("length of list", len(fruits))
#
#
# # while loop
# index = 0
# while index < len(fruits):
#     print(fruits[index])
#     index += 1
#
#
# # list function example:
# list1 = [1, 3, 4, 7, 9, 13]
#
# print(len(list1))
# print(min(list1))
# print(max(list1))
# print(sum(list1))


