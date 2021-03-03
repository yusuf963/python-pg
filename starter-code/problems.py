import math
from functools import reduce

# write a function that returns "Hello World!" if no argument is given, or "Hello <argument>!" otherwise
# eg: hello() => "Hello World!"; hello("Mike") => "Hello Mike!"
def hello(string='World'):
  return f'Hello {string}!'


# write a function that will calculate the area of a circle, given the radius
def area_of_circle(radius):
  return math.pi * (radius ** 2)


# write a function to convert celcius to farenheit
def celcius_to_farenheit(celcius):
  return celcius * 9 / 5 + 32


# write a function that will reverse a number (eg. 456733 become 337654)
def number_reverse(number):
  new_str = str(number)[::-1]
  return float(new_str)


# write a function to check if a word or phrase is a palindrome returning a boolean
# eg. palindrome_check('dad') => True, palindrome('nonsense') => False
def palindrome_check(string):
  clean_str = string.replace(' ', '')
  return clean_str == clean_str[::-1]


# write a function that returns the letters of a word or phrase in alphabetical order case insensitive
# eg. order_string_alphabetically('javascript is cool') => 'aacciijlooprsstv'
def order_string_alphabetically(string):
  string_list = list(string.casefold())
  string_list.sort()
  return ''.join(string_list).strip()


# write a function that capitalizes the first letter of each word
# eg. title_case('the lord of the rings') => 'The Lord Of The Rings'
def title_case(string):
  return string.title()


# write a function that returns the number of vowels in a string case insensitive
# 'y' should not be considered a vowel
# eg: num_of_vowels('Yellow Submarine') => 6
def num_of_vowels(string):
  clean_str = string.casefold()
  count = 0
  for vowel in 'aeiou':
    count = count + clean_str.count(vowel)
  return count


# write a function that frames a string in asterisks (*)
#                             ***************
# eg: frame('Hello Kitty') => * Hello Kitty *
#                             ***************
def frame(string):
  return f'''{'*' * len(string) + '*' * 4}
* {string} *
{'*' * len(string) + '*' * 4}'''


# write a function which returns all the string elements in a list
# eg: strings_only([10, 'Mike', '23', {}, 'elephant']) => ['Mike', '23', 'elephant']
def strings_only(array):
  return list(filter(lambda element: type(element) == str, array))


# write a function that returns the total number of characters in a list of words
# eg: character_count(['Stay', 'hungry', 'stay', 'foolish']) => 21
def character_count(array):
  return len(''.join(array))


# using any list method, write a function that returns the product of a list (ie the values multiplied by each other). Your function should convert strings to numbers, and should only return a positive number
# eg: positive_product([5, 12, 6]) => 360, positive_product([-14, 8, 9]) => 1008
def positive_product(array):
  return reduce(lambda sum, elem: sum * abs(elem), array, 1)


# write a function that returns the string elements of a list that have a given number of characters or larger
# eg: words_of_length(['emu', 'caterpiller', 'rooster'], 4) => ['caterpiller', 'rooster']
def words_of_length(array, min_length):
  return list(filter(lambda word: len(word) >= min_length, array))
