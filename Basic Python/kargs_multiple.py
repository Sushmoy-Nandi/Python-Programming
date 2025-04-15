def full_name(first, last):
    name = f'Full name is: {first} {last}'
    return name

# take parameters in order(serial wise)
# name = full_name('Sushmoy', 'Nandi')
name = full_name(last='kodu',first='alu')
print(name)

# def famous(**kargs)
def famous_name(first, last, **addition):
    name =f'{first} {last}'
    # print(addition['title'])
    for key, value in addition.items():
        print(key,value)
    return name

name = famous_name(first='abc',last='abd',title='Atc',tille2='ato',last2='abd2')
print(name)

# def function_name(num1,num2, *args, **kargs):


# return multiple things from an array
def a_lot(num1,num2):
    sum =num1+num2
    mult=num1*num2
    remain =num1-num2
    # return [sum,mult,remain]
    return sum,mult,remain

everything = a_lot(55,21)
print(everything)