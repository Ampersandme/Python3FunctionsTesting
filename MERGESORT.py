import random

def merge(X, Y):
    " merge two sorted lists "
    p1 = p2 = 0
    out = []
    while p1 < len(X) and p2 < len(Y):
        if X[p1] < Y[p2]:
            out.append(X[p1])
            p1 += 1
        else:
            out.append(Y[p2])
            p2 += 1
    out += X[p1:] + Y[p2:]
    return out


def mergeSort(A):
    if len(A) <= 1:
        return A
    if len(A) == 2:
        return sorted(A)

    mid = len(A) / 2
    return merge(mergeSort(A[:int(mid)]), mergeSort(A[int(mid):]))

if __name__ == "__main__":
    # Generate 20 random numbers and sort them
    A = [random.randint(1, 100) for i in range(20)]
    print (A)
    print (mergeSort(A))
