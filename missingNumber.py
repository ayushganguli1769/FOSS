t = int(input())
for _ in range(t):
    n = int(input())
    #numberMap = hashMap()
    arr = list(map(int,input().rstrip().split()))[:n]
    bool_array = [False]*n
    for val in arr:
        bool_array[val-1] = True
    for i in range(0,n,1):
        if bool_array[i] == False:
            print(i+1)
            break
        