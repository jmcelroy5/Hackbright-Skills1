# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    odd_list = []
    for num in number_list:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list

print all_odd(number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    even_list = []
    for num in number_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

print all_even(number_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_list = []
    for word in word_list:
        if len(word)>= 4:
            long_list.append(word)
    return long_list

print long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    min = number_list[0]
    for num in number_list:
        if num < min:
            min = num  
    return min

print smallest(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    max = number_list[0]
    for num in number_list:
        if num > max:
            max = num  
    return max

print largest(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    halves = []
    for num in number_list:
        num = float(num)
        halves.append(num/2)
    return halves

print halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    word_length = []
    for word in word_list:
        word_length.append(len(word))
    return word_length

print word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    total = 0
    for num in number_list:
        total = total + num
    return total

print sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    ans = 1
    for num in number_list:
        ans = ans * num
    return ans

print mult_numbers(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    joined = ""
    for word in word_list:
        joined = joined + word
    return joined

print join_strings(word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    average = sum_numbers(number_list)/len(number_list)
    return average

print average(number_list)
