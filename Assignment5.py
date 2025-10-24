# Assignment:- 5  on loops

# 1: print in the same line
# print("Hello", end = " ")
# print("xyz")

# print("Hello", "Rohit", sep = "*", end = " * ")
# print("Rohit")


# while loop to print the output in the same line
# i = 1
# while i < 4:
#     print(f"Hello Rohit {i}", end = " ")
#     i += 1


# i = 1
# while i < 4:
#     print(f"Hello{i}", "Rohit", sep = "*", end = " ")
#     i +=1


# 2: star patterns
# n = 5  # number of rows
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end = " ")
#     print()

# shortcut method
# n = 5
# for i in range(1, n+1):
#     print("* " * i)



# inverted triangle
# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print("*", end = " ")
#     print()

# shortcut method
# for i in range(n, 0, -1):
#     print("* " * i)


# Equilateral triangle
# n = 5
# for i in range(1, n+1):
#     print(' ' * (n - i), end = " ")
#     print("*" * (2 * i - 1))



# 3: Factorial of a number
# def factorial(n):
#     result = 1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result
# print(factorial(5))



# 4: count vowels in a string
# my_string = "India is the second largest country according to population"
# vowels = "aeiou"
# count = 0
# for char in my_string:
#     if char.lower() in vowels:
#         count += 1
# print("Numbers of vowels are:-", count)



# 5: Longest word in sentence
# sentence = "India is the second largest country according to population"
# words = sentence.split()      # ['India', 'is', 'the', 'second', 'largest', 'country', 'according', 'to', 'population']
# longest_word = ""
# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word
# print("The longest word is:", longest_word)



# 6: do-while loop in python
# while True:
#     num = int(input("Enter a number greater than 10: "))
#
#     if num > 10:
#         print(f"Valid number entered: {num}")
#         break   #exit the loop when condition is satisfied
#     else:
#         print("Number is not greater than 10, try again")



# Fibonacci sequence
def fibonacci(n):
    a,b = 0,1
    count = 0
    while count < n:
        print(a)
        a,b = b, a+b
        count += 1
fibonacci(10)
