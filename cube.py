def cube(number):
    return number*number*number
def div_3(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(div_3(2))