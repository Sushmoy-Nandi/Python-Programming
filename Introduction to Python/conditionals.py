# in, not, not in, is, is not
a=2
if a>5:
    print('5 er besi')
elif a>3:
    print("3 ar boro")
elif a==2:
    print("akdom 2 ar soman soman")
else:
    print("5 er kom")

boss =True

if boss is True:
    print("Boss is true")
else:
    print("Boss is false")

if boss is not True:
    print("Boss is true")
else:
    print("Boss is false")

coin ='head'
if boss==True:
    print("Boss you are good")
    if coin == 'tail':
        print("bating")
    else:
        print("bowling")
else:
    print("You are not a good boss")
