# what other libraries
libraries = ['pandas', 'numpy', 'flask']

print(libraries)

for lib in libraries:
    print(lib)

first_thing = libraries[0]
last_thing = libraries[-1] #cool trick

things_in_list = len(libraries)
print(f'There are {things_in_list} things in my list')