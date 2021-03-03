
# !  if elif else
a = 5
if a == 10:
    b = 10
elif a > 10 or a == 5:
    b = 11


# ! while
while a > 0 and b == 10:
    print('Ayman')
    a -= 1

    # ! for in on list
names = ['Agnetha', 'Benny', 'Björn', 'Anni-Frid']
for name in names:
    print('hello ', name, '!')
    print(f' it is {name}\'s book!')
   # ! for in on dict
car = {'make': 'Fiat', 'model': 'Uno', 'color': 'red'}
for adj in car:
    print(car[adj])

# ! Range
for i in range(10+b):
    if i % 2 == 0:
        print(i)
    elif i == 7:
        print('# heeey its seven')
    elif i == 9:
        b = i + 1
        print(i, 'heeeey it odd number')
    elif i == 11:
        break
    else:
        print('heeeey it odd number')

 #! Boolean Logic
c = 100
t = 6
print(c != t)
print(c > 6 and t < 7)


# ! cheking the type of triangle, scalene345/isoceles553/equilateral555
def cheking_triangle(a, b, c):
    if a or b or c < 0:
        print(
            'the length of a triangle can not be 0 or less, please provide a valied side length')
    if a and b and c > 0:
        if a == b and b == c and a == c:
            print('this triangle is equilateral')
        elif a != b and b != c and a != c:
            print('this triangle is scalene')
        else:
            print('this triangle is isoceles')


cheking_triangle(1, 1, 398651)


# !Ternary operator
j = 10
k = 5 if j > 10 else 20
print(k)
