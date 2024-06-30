#!/bin/python3

import sys
def check_palindrome(n):
    sum = 0
    temp = n
    while temp>0:
        digit = temp%10
        sum = sum*10+digit
        temp = temp//10
    if sum == n:
        return 1
    else:
        return 0

def palin(n):
    temp = n
    while (check_palindrome(temp)==0):
        temp -=1
    return temp

list1 = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    list1.append(palin(n))

for i in list1:
    print(i)
