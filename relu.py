
def ReLU(number):
    #if number is positive, return number
    #else, return 0
    if number > 0:
        return number
    else:
        return 0


print(ReLU(10))
print(ReLU(-1))