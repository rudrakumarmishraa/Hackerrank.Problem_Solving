#!/bin/python3
import os

def diagonalDifference(arr):
    i=0
    s1=0
    s2=0
    while i<len(arr):
        s1=s1+arr[i][i]
        s2=s2+arr[i][len(arr)-i-1]
        i=i+1
    return abs(s1-s2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()