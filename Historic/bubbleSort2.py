#!/usr/bin/python

input_list = [13,12,10,1,2,11]

print (input_list)

def bubblesort(bubble_list):
    for i in range(len(bubble_list)):
        for j in range(i):
            if int(bubble_list[j]) > int(bubble_list[j+1]):
                bubble_list[j],bubble_list[j+1] = bubble_list[j+1],bubble_list[j]
    output_list = bubble_list
    print (bubble_list)
    return output_list


A = bubblesort(input_list)
bubblesort(A)
