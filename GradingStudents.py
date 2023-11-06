#!/bin/python3
import os

def gradingStudents(grades):
    i = 0
    result = []
    while(i<len(grades)):
        print(grades[i])
        if(grades[i]>=38):
            if(grades[i]%5 == 0):
                result.append(grades[i])
            elif((grades[i]+1)%5==0):
                result.append(grades[i]+1)
            elif((grades[i]+2)%5==0):
                result.append(grades[i]+2)
            else:
                result.append(grades[i])
        else:
            result.append(grades[i])
        i+=1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()