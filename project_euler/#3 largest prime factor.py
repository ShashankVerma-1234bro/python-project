#!/bin/python3

import sys

def check_prime(n):
    flag = 1
    for i in range(2,n):
        if n%i == 0:
            flag = 0
            break
        else: flag = 1
    if flag == 1:
        return True
    else:
        return False

t = int(input().strip())
num = []

for a0 in range(t):
    
    n = num.append(int(input().strip()))
    

for i in num:
    prime= []
    for j in range(2,i+1):
        if (i%j == 0) and (check_prime(j)):
            prime.append(j)
    
    print(max(prime))
