n = int(input().strip())

list1 =[]

def factorial(number):
    fact = 1
    while number >0:
        fact = fact*number
        number = number -1
    return fact

def summation(number):
    sum = 0
    while number>0:
        sum = sum + number%10
        number = number//10

    return sum

for i in range(n):
    number = int(input().strip())
    list1.append(summation(factorial(number)))

for i in list1:
    print(i)
