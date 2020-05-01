def fn(arr,n):
    left_array = [0]*n
    right_array = [0]*n
    maxi = -sys.maxsize
    mini = sys.maxsize
    for i in range(n):
        if arr[i] >= maxi:
            maxi = arr[i]
            left_array[i] = 1
    for i in range(n-1,-1,-1):
        if arr[i] <= mini:
            mini = arr[i]
            right_array[i] = 1
    for i in range(1,n-1,1):
        if left_array[i] == 1 and right_array[i] == 1:
            return arr[i]
    return -1
import sys
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().rstrip().split()))[:n]
    print(fn(arr,n))

    