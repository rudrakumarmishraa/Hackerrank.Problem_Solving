#!/bin/python3

import os
def camelcase(s):
    words = 1
    for i in list(s):
        if(i.isupper()):
            words+=1
    return words

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = camelcase(s)
    fptr.write(str(result) + '\n')
    fptr.close()
