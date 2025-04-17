name = 'Sakib\'s Khan'
name2 = "Shakib Khan2"
name3 = """
        Shakib Khan
        number one
"""

print(name)
# string is a sequence of characters
for char in name2:
    print(char)

print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])
# mutable means changeable
# immutable means you can not change it
# name2[0]='R'
print(name2)

if 'Khan' in name2:
    print('exists')

print(name2.upper())