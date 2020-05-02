
# This function should rotate list counter-
# clockwise by k and return new head (if changed) 
def rotateList(head, k):
    curr = head
    i = 0
    prev = None
    #print(k,"k")
    while i != k :
        if curr:
            #print(curr.data)
            prev = curr
            curr = curr.next
        else:
            #print("head returned")
            return head
        i += 1
    #print(prev.data,"prev")
    if curr: # case if curr.next becomes None
        #print(curr.data,"curr")
        prev.next = None
        new_head = curr
        while curr.next is not None:
            curr = curr.next
        #print(curr.data,"last pointer")
        curr.next = head
    else:
        #print("No current")
        return head
    return new_head
