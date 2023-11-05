#!/bin/python3

def staircase(n):
    for i in range(1, n+1):
        print(f"{' '*(n-i)}{'#'*i}")
if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)