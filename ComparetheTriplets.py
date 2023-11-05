#!/bin/python3
import os

def compareTriplets(a, b):
    alice = 0
    bob = 0
    i = 0
    length = len(a)
    while(i<length):
        if(a[i]>b[i]):
            alice+=1
        elif(b[i]>a[i]):
            bob+=1
        i+=1
    return alice, bob

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()