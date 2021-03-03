

# ! Map

from functools import reduce
nums = [10, 2, 3, 6, 6]


def double(num):
    return print(num * 2)


double(10)
num1 = list(map(lambda num: num * 2, nums))
print(num1)


# ! filtering
even_num = filter(lambda num: num % 2 == 0, nums)
print(list(even_num))


# ! reduce
num_to_sum = [33, 55, 6]
summed = reduce(lambda total, num: total + num,
                num_to_sum,
                0)
print(summed)

doubled = [num * 2 for num in num_to_sum]
print(doubled)


less_five = [num > 33 for num in num_to_sum]
print(less_five)
less_five1 = [num for num in num_to_sum if num > 33]
print(less_five1)
# ! convert to dict
listy = ['Ali', 'Emma', "Nick"]
name_dict = {i: item for i, item in enumerate(listy)}
print(name_dict)

# !
duplicate_nums = [1, 2, 3, 1, 4, 5, 6, 4, 5]
set_num = {num for num in duplicate_nums}
print(set_num)

name = input('what is you name?')
color = input('what is your color')
print('Hi '+name + ' your favorite is '+color)


duplicate_Char = ['f', 'f', 'erw']
set_char = {char for char in duplicate_Char}
print(set_char)
