numbers= [12,56,98,78,56,12,26,98]
person1=['kala chan','kalipur',23,'student']
# key value pair
# dictionary
# object
# hash table
# overlap with set
# {key: value, key: value, key: value}
person = {'name': 'Sushmoy Nandi','address':'Dhaka','age':23,'job':'No Job'}

print(person)
print(person['job'])
print(person.keys())
print(person.values())

person['language'] = 'Python'
person['name'] = 'Bappi'
del person['age']
print(person)

# special dictionary looping
for item in person:
    print(item)

for key, value in person.items():
    print(key,':',value)