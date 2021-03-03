import sys
import timeit
# print(dir(sys))
# print(help(sys.getsizeof))
# ! strings
str_0 = 'hello'
str_1 = "hello"
str_2 = "Yusuf\'s laptop"
str_3 = 'Yusuf said, \'laptop\''

# ! multible line strings
multi_line = '''
In python we can also use three quote marks around a string, which means that we can use carriage returns, tabs and quotes within the string. This is very similar to "ES6" backticks
'''

str_4 = 'This\'ll not come out quite as expected Holmes'

# !numbers
# print(type(15))
# print(type(1.8))

# ! Boolean
# print(type(True))
# print(type(False))


# ? falsy value in python
# None # same as null
# False
# 0
# 0.0
# ''
# [] # an empty list (equivalent to an empty array in JS)
# {} # an empty dict (equivalent to an empty object in JS)
# () # an empty tuple (an immutable array)
# set() # an empty set
# range(0)
# ! list
list = [10, 'Python', True, 'hamster']
# print(list.clear())
# print(dir(list))
# print(list)
# list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=100000)
# tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=100000)
print(list[0:3:2])

# ! Dictionary
dict = {'name': 'Julien', 'role': 'Regional director'}
dict['age'] = 30
dict.keys()
dict.values()
print(dict)
