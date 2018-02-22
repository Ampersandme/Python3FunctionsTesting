import random

input_list = [random.randint(1, 100) for i in range(80)]

print (input_list)

def bubblesort(bubble_list): #two level bubblesort
    for i in range(len(bubble_list)):
        for j in range(i):
            if int(bubble_list[j]) > int(bubble_list[j+1]):
                bubble_list[j],bubble_list[j+1] = bubble_list[j+1],bubble_list[j]
    output_list = bubble_list
    print (bubble_list)
    return output_list



def completeBubble(bubble): #redefines the two level sort, cycles till a sort yeilds no change in number positions
    A = bubblesort(bubble)
    B = bubblesort(A)
    while A == B:
        C = bubblesort(A)
        D = bubblesort(B)
        A == C and B == D
        if A == B:
            print ("Looks sorted to me, eh")
            break

completeBubble(input_list)
