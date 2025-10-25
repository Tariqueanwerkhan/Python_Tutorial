# Assignment-6
# on list, tuple set and dict

# Q1 Find the Intersection (common elements) of Two Lists?
list1 = [1,3,4,5,7,8,10]
list2 = [7,8,9,10,12,13]

# using for loop
def intersection_loop(lst1, lst2):
    common_list = []
    for item in lst1:
        if item in lst2 and item not in common_list:
            common_list.append(item)
    return common_list
print(intersection_loop(list1, list2))

# using list comprehension
def intersection_comp(lst1, lst2):
    return [item for item in lst1 if item in lst2]
print(intersection_comp(list1, list2))



# Q2 Find the Most Frequent Element in a List?
numbers = [1,2,2,2,3,3,4,4,4,4,5,5,2,6,6,2,7,8,2,2,4]
def most_freq(lst):
    max_count = 0
    most_freq = None
    for item in lst:
        count = lst.count(item)
        if count > max_count:
            max_count = count
            most_freq = item
    return most_freq
print(most_freq(numbers))


# Q3 find cumulative sum of a list
numbers = [1, 2, 3, 4, 5 , 6, 7, 8]
def cumulative_sum(lst):
    cum_sum = []
    total = 0
    for num in lst:
        total += num
        cum_sum.append(total)
    return cum_sum
print(cumulative_sum(numbers))


# Q4 Remove duplicates from a list
fruits = ["apple", "banana", "apple", "mango", "banana", "apple"]
def remove_duplicates(lst):
    unique = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique
print(remove_duplicates(fruits))



# Q5 Find the index of an element in a tuple
my_tuple = (3, 6, 1, 10, 15, 12, 7, 20, 9)
def find_index(tup, element):
    if element in tup:
        return tup.index(element)
    else:
        return -1
print(find_index(my_tuple, 10))


# alternate method
# def find_tuple(tup, element):
#     return tup.index(element) if element in tup else -1
# print(find_tuple(my_tuple, 12))




# Q6 Find the most frequent value in a dictionary
data = {'a': 2, 'b': 4, 'c': 2, 'd': 3, 'e': 2, 'f': 4, 'g': 5}
def most_freq(dct):
    frequency = {}
    for value in dct.values():
        if value not in frequency:
            frequency[value] = 0
        frequency[value] += 1
        max_value = max(frequency, key = frequency.get)
        return max_value
print(most_freq(data))



# Q7 Merge Dictionaries with summation
dict1 = {'a': 5, 'b': 25, 'c': 10}
dict2 = {'b': 17, 'c': 34, 'd': 22}
def merge_dict(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
print(merge_dict(dict1, dict2))

