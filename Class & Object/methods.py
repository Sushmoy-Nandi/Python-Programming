def call():
    print('calling someone I do not konw')
    return 'call done'


class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camera','speaker','hammer']


    def call(self):
        print('calling one person')
    
    def send_sms(self,phone, sms):
        text = f'sending SMS to: {phone} and messege: {sms}'
        return text

my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(10119, 'I forgot to miss you')
print(result)