numbers=[45,87,65,43,85,14,26,61]
odds=[]
for num in numbers:
    if num % 2 == 1:
        odds.append(num)
print(odds)

odd_nums=[num for num in numbers if num % 2== 1]
print(odd_nums)

players=['Sakib','Musfik', 'Liton']
ages = [39,38,32]

for player in players:
    print('Player: ',player)
    for age in ages:
        print(player,age)

age_comb=[]
for player in players:
    print('Player:',player)
    for age in ages:
        print(player,age)
        age_comb.append([player,age])
print(age_comb)

age_comb2=[[player,age] for player in players for age in ages]
print(age_comb2)