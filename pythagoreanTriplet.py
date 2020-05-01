def has_triplet(arr,n):
    for i in range(n-1,1,-1):
        j = 0
        k = i -1
        while j <k:
            if pow(arr[j],2) + pow(arr[k],2) == pow(arr[i],2):
                return True
            elif pow(arr[j],2) + pow(arr[k],2) <= pow(arr[i],2):
                j += 1
            else:
                k -= 1
    return False  
                
t= int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().rstrip().split()))[:n]
    arr = sorted(arr)
    if has_triplet(arr,n):
        print("Yes")
    else:
        print("No")
