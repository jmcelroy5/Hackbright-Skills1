"""
Attempting to come up with new solutions for skills1 exercise
that utilize Python functions reduce, map, and filter.
"""

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    def odds(num): return num % 2 != 0
    return filter(odds,number_list)

print all_odd(number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    def evens(num):return num % 2 == 0
    return filter(evens,number_list)

print all_even(number_list)

# Write a function that takes a list of strings and makes a new list with all strings of length 4 or greater.
def long_words(word_list):
    def long(word): return len(word) >= 4
    return filter(long,word_list)

print long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    def small(a,b): 
        if a < b or a == b:
            return a 
        else:
            return b
    return reduce(small, number_list)

print smallest(number_list)

# Re-write smallest with lambda function
def smallest2(number_list):
    func = lambda a,b: a if (a<b) else b
    return reduce(func, number_list)

print smallest2(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    def large(a,b):
        if a > b or a == b:
            return a
        else:
            return b
    return reduce(large, number_list)

print largest(number_list)

# Re-write largest with lambda function
def largest2(number_list):
    func = lambda a,b: a if (a>b) else b
    return reduce(func, number_list)

print largest2(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    def half(num): return num / 2.0
    return map(half, number_list)

print halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    def length(word): return len(word)
    return map(length,word_list)

print word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    def adding(a,b): return a + b
    return reduce(adding, number_list)

print sum_numbers(number_list)

# Rewrite sum_numbers with lambda function.
def sum_numbers2(number_list):
    return reduce(lambda x,y: x+y, number_list)

print sum_numbers2(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    def mult(a,b): return a*b
    return reduce(mult,number_list)

print mult_numbers(number_list)

# Rewrite mult_numbers using lambda function.
def mult_numbers2(number_list):
    return reduce(lambda a,b: a*b, number_list)

print mult_numbers2(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string. 
def join_strings(word_list):
    def joinwords(a,b): return a+b
    return reduce(joinwords,word_list)

print join_strings(word_list)

# Re-write join_strings with lambda function
def join_strings2(word_list):
    return reduce(lambda a,b: a + b, word_list)

print join_strings2(word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return sum_numbers(number_list)/len(number_list)

print average(number_list)
