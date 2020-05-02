string_list = []
def findPermutation(list_string,curr_index,max_index):
    #print(list_string,curr_index)
    global string_list
    if curr_index == max_index:
        permutation_string = ""
        #print(list_string)
        for char in list_string:
            permutation_string += char
        string_list.append(permutation_string)
        """
        string_list.append(list_string)
        """
        return 
    for i in range(curr_index,max_index +1):
        new_string = list_string[:]
        #print("Swapping ",new_string[curr_index],new_string[i])
        (new_string[curr_index],new_string[i]) = (new_string[i],new_string[curr_index])
        #print(list_string,"gives",new_string,"i=",i,"at cur_index=",curr_index)
        findPermutation(new_string,curr_index+1,max_index)

        
t = int(input())
for _ in range(t):
    string_list = []
    my_string = str(input())
    list_string = list(my_string)
    max_index = len(list_string)-1
    
    findPermutation(list_string,0,max_index)
    string_list = sorted(string_list)
    #print(string_list)
    for per_string in string_list:
        print(per_string,end=" ")
    print()
    """
    for sub_string_list in string_list:
        for char in sub_string_list:
            print(char,end="")
        print(end=" ")
    print()
    """
    #print(string_list)