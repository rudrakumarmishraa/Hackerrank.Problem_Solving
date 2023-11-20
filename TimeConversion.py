import os

def timeConversion(s):
    hr = s[0:2]
    minSec = s[3:8]
    fr = s[8:10]
    if(fr=='AM'):
        if(hr=='12'):
            return '00:'+minSec
        else:
            return s[0:8]
    # []
    else:
        if(hr=='12'):
            return '12:'+minSec
        else:
            return str(int(hr)+12)+':'+minSec

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
