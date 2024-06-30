def sum_prime(n):
    list1 = []
    for i in range(2,n+1):
        if check_prime(i):
            list1.append(i)
    return sum(list1)

def check_prime(n):
    flag = 1
    for i in range(2,round(n**0.5)+1):
        if n%i == 0:
            flag = 0
            break
        else:
            flag = 1
    if flag == 1:
        return 1
t = int(input().strip())
list2 = []
for i in range(t):
    num = int(input().strip())
    list2.append(sum_prime(num))

for i in list2:
    print(i)
