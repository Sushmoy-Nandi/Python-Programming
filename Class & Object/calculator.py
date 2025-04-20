class Calculator:
    brand = 'Casio MS990'

    def add(self,num1,num2):
        sum= num1+num2
        return sum
    def deduct(self,num1,num2):
        substraction=num1-num2
        return substraction

    def mul(self,num1,num2):
        multiply = num1*num2
        return multiply
    def div(self,num1,num2):
        divide = num1/num2
        return divide


my_calculator = Calculator()

print(my_calculator.add(10,5))
print(my_calculator.deduct(10,5))
print(my_calculator.mul(10,5))
print(my_calculator.div(10,5))

