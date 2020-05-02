t = int(input())
for _ in range(t):
    str_array = list(map(str,input().rstrip().split('.')))
    n = len(str_array)
    my_string = ""
    while n > 1:
        n -= 1
        my_string += str_array.pop() + "."
    my_string += str_array.pop()
    print(my_string)