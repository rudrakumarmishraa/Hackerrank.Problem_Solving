#!/bin/python3
def plusMinus(arr):
    i = 0
    pos = 0
    neg = 0
    zero = 0
    while(i<len(arr)):
        if(arr[i]>0):
            pos+=1
        elif(arr[i]<0):
            neg+=1
        else:
            zero+=1
        i+=1
    print(pos/(len(arr)))
    print(neg/(len(arr)))
    print(zero/(len(arr)))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)