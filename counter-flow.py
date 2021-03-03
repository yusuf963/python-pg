
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
