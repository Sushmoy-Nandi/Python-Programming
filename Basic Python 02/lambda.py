# lambda

# def doubled(x):
#     return x*2

def doubled(num): return num * 2
def squared(num): return num * num


result = doubled(44)
output = squared(9)
print(result, output)


def add(x, y): return x+y


sum = add(11, 33)
print(sum)

numbers = [12, 56, 98, 78, 56, 12, 6, 98]
# doubled_nums = map(doubled, numbers)
doubled_nums = map(lambda x: x*2, numbers)
squared_numbers = map(lambda x: x*x, numbers)
print(numbers)
# print(list(doubled_nums))
print(list(squared_numbers))


actors = [
    {'name': 'sabana', 'age': 65},
    {'name': 'sabnoor', 'age': 45},
    {'name': 'sabila noor', 'age': 30},
    {'name': 'srabonti', 'age': 38},
    {'name': 'shaon', 'age': 47},
]

juniors = filter(lambda actor: actor['age'] < 40, actors)
Fivers = filter(lambda actor : actor['age'] %5==0, actors)
# print(list(juniors))
print(list(Fivers))
