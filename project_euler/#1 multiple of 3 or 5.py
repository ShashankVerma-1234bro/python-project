def summation(number):
    sum1 = 0
    for i in range(1,number):
        if ((i%3 == 0) or (i%5 == 0)):
            sum1 = sum1 + i
    return sum1
list1 = []
for i in range(2):
    n = int(input().strip())
    list1.insert(i,n)

for i in list1:
    print(summation(i))


