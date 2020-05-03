t = int(input())
for _ in range(t):
    n = int(input())
    arrival = list(map(int,input().rstrip().split()))[:n]
    dept = list(map(int,input().rstrip().split()))[:n]
    arrival.sort()
    dept.sort()
    #print(arrival)
    #print(dept)
    needed_platform = 1
    max_platform = 1 # as atleast one platform needed for a train# max of number of platform required in each case which is min platform toally
    i = 1# arrival pointer
    j = 0#departure pointer
    while i < n and j< n:
        if dept[j] >= arrival[i]:
            #print(dept[j],arrival[i],"dept arrival increasing platform")
            i += 1
            needed_platform += 1
            #print(needed_platform,"needed platform")
            if needed_platform > max_platform:
                max_platform = needed_platform
        else:
            #print(dept[j],arrival[i],"dept arrival decreasing platform")
            j += 1
            if needed_platform > 0:
                needed_platform -= 1
            #print(needed_platform,"needed platform")
    print(max_platform)
            