#input of how many times
#take power as input
#create a list
#create sum function to get sum of asnwer and append to list
#for loop in list
list1 = []
def summation(power):
    number = 2**power
    digit = 0
    ans = 0
    while number>0:
        digit = number%10
        ans = (ans)+digit
        number = number//10

    return ans

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    list1.append(summation(n))

for i in list1:
    print(i)
