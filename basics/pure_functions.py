
from functools import reduce

# pure function
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list

from functools import reduce


def multiply_by2(item):
    return item * 2

#map function
print(list(map(multiply_by2,[1,2,3])))

my_list = [1,2,3,4,5,6]
def only_odd(item):
    return item % 2 != 0

# filter function 
print(list(filter(only_odd, my_list)))

your_list = [10,20,30]

# zip function
print(list(zip(my_list, your_list)))

def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, my_list, 0))
print('-------------------------')

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capital(item):
    return item.upper()
print(list(map(capital, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def filter_score(item):
    return item > 50

print(list(filter(filter_score,scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def combine_numbers(acc , item):
    return acc + item

print(reduce(combine_numbers, (scores + my_numbers)))