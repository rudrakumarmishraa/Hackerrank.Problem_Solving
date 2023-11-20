def miniMaxSum(arr):
    arr.sort()
    minimum = 0
    maximum = 0
    for i in range(4):
        minimum+=arr[i]
    for i in range((len(arr)-1), (len(arr)-5), -1):
        maximum+=arr[i]
    print(minimum, maximum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
