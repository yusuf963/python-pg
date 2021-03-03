

import random
import math
string = "this is string"
string1 = 'this is another one'
# print(string)
# print(type(string))
# print(isinstance(string, str))
formatted_string = f'hello {string}'
# print(formatted_string)

name = "Yusuf"
coffe = 1
yusuf_coffee = f"{name} {coffe}"
print(yusuf_coffee)


# ! number
print(math.ceil(1.6))
# print(random.random() * 10)


# ! booolean
print(type(True))


# falsy value
# 0
# 0.0
# false
# [] called list
# {}
# ''
# none
# (,)
# set()
# range(0)

# ! logical operator
print(True and False)
print(not (True and False and (False or True)))
print(True == 'True')


# ! if else operator
a = 10
if a > 10:
    print('its greater')
elif a == 10:
    print('its equal')

    # ! ternaries
    value = 'horray' if a > 10 else 'bla'
    print(value)
    if a == 10:
        print('less than 10')
