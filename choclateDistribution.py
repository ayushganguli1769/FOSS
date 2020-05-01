import sys
t = int(input())
for _ in range(t):
    n = int(input())#number of packets
    arr = list(map(int,input().rstrip().split()))
    arr = sorted(arr)
    m = int(input())#number of students
    min_diff = sys.maxsize
    for i in range(len(arr)-m+1):
        local_diff = arr[i+m-1] - arr[i]
        if local_diff < min_diff:
            min_diff = local_diff
    print(min_diff)