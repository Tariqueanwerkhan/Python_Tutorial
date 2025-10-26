# sets in python

# characteristics of sets
# - unique values
# - unordered - no indexing
# - mutable - add/remove elements
# - immutable elements - replace/modify existing elements

# create set suing curly braces
# my_set = {1, 2, 3, 4, 5, 6}
# print(my_set)
# print(type(my_set))
#
#
# # create set using set constructor
# my_set2 = set([7, 8, 9, 10])
# print(my_set2)
#
# # ste operations
# # adding elements
# numbers = {1, 2, 3, 4, 5}
# numbers.add(6)
# print(numbers)
#
#
# # removing elements
# fruits = {'apple', 'banana', 'orange', 'strawberry'}
# fruits.remove('orange')
# print(fruits)
#
# # discard
# fruits.discard('apple')
# print(fruits)


# set methods
# 1. union - combine elements from 2 sets
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
union_set = set1.union(set2)
print(union_set)

# union alternative
union_set2 = set1 | set2
print(union_set2)


# 2. Intersection - comma elements
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
inter_set = set1.intersection(set2)
print(inter_set)

# intersection alternative
inner_set2 = set1 & set2
print(inner_set2)


# difference - element present in first set only but not in second set
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
diff_set = set1.difference(set2)
print(diff_set)

# difference alternative
diff_set2 = set1 - set2
print(diff_set2)


# 4. symmetric difference - element in either set but not in both
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
sdiff_set = set1.symmetric_difference(set2)
print(sdiff_set)

# symmetric alternative
sdiff_set2 = set1 ^ set2
print(sdiff_set2)



# set iteration
# for loop
numbers = {1,2,3,4,5,6}
for i in numbers:
    print(i)


# set comprehension
squares = {x**2 for x in range(1,10)}
print(squares)



