# CSV comma separated value
# .txt text file

# with open('meessage.txt','w') as file:
#     file.write('I love you, Python')
# with open('meessage.txt','a') as file:
#     file.write('I love you, Python')
with open('meessage.txt','r') as file:
    text = file.read()
    print(text)