#!/bin/python3
import os

def birthdayCakeCandles(candles):
    result = 0
    biggest = 0
    for i in candles:
        if(i>biggest):
            biggest = i
    for i in candles:
        if(i==biggest):
            result+=1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()