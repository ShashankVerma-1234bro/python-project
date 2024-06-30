#!/bin/python3

import sys

def f1(n):
    return (sum(list(range(1,n+1))))**2 - (sum([x**2 for x in range(1,n+1)]))
list1 = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    list1.append(f1(n))

for i in list1:
    print(i)
