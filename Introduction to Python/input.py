# print('Now I need money')
# input()

# input('Give me some money: ')
# money= input('Give me some money: ')
# print("Here is your money",money)

first_money=input('Ayan, Dosto kichu taka dey: ')
second_money=input('Pranto, Dosto kichu taka dey: ')
print(type(first_money))
# by default the input from user will be string type
print('money I got from Ayan',first_money,'and from Pranto',second_money)
first_money_int=int(first_money)
second_money_int=int(second_money)
print(type(first_money_int))
# total=first_money+second_money
total=first_money_int+second_money_int
print('Total money I got: ',total)
