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
        sum = sum + factorial(number%10)
        number = number//10
    return sum
count = 0

for i in range(10,n+1):
    if summation(i)%i == 0:
        count+=i

print(count)
