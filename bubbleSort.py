#!/usr/bin/python
import random

A = [random.randint(1, 100) for i in range(20)]
input_list = A

def bubblesort(hello123):
    for i in range(len(hello123)):
        for j in range(i):
            if int(hello123[j]) > int(hello123[j+1]):
                hello123[j],hello123[j+1] = hello123[j+1],hello123[j]

print (A)
print (bubblesort(input_list))
