def triangle_number(n):
    return n*(n+1)/2

def number_pos(n):
    return int((-1 + round((1+(8*n))**0.5))/2)

t = int(input().strip())
list1 = []
for i in range(t):
    n = int(input().strip())
    list1.append(n)

max_num = number_pos(max(list1))
numbers = [triangle_number(x) for x in range(1,max_num)]
list2 = []

for i in list1:
    


