#comment whatever

print('Hello capstone')
school = 'MCTC'
gpa = 3.7
students_in_class = 22

# if statements

if gpa == 4:
    print('WOW')
elif gpa > 3:
    print('Awesome')
else:
    print('Cool')


#lists 
schools = ['MCTC','DCTC', 'North Hennepin']

if 'MCTC' in schools:
    print('MCTC is one of the schools in the list')

schools.sort
print(schools)
schools.append('U of M')
print(schools)
print(schools.reverse()) # schools.reverse() returns none

#strings
class_name = 'Software Development Capstone'
print(class_name.upper())
print(len(class_name))
print(class_name.split())
print(class_name.split('o'))

if 'Capstone' in class_name:
    print('This is the capstone')



#loops 
for x in range (10):
    print(x)

for s in schools:
    print(s.upper())

for letter in school:
    print(letter * 10)

data = [0] * 10
print(data)

more_data = [None] * 10
print(more_data)

#while loops

while not name:
    print('Eneter at least one character')
    name = input('Enter your name: ')

# true false and none

start_of_semester = True
winter = False

if winter:
    print('brr!')
else:
    print('its not winter')

#dictionaries 

class_codes = {2905: 'Capstone', 2560: 'Web', 2545: 'Java'}

for code in class_codes:
    print(code)
    print(class_codes[code])

for code, name in class_codes.items():
    print('the class code is ' + str(code) + ' and the name is ' + name)