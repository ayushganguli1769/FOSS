#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
def isPalindrome(head):
    if head.next is None:
        return 1
    slow_p = head
    fast_p = head

    i = 0
    while slow_p and fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p= fast_p.next.next
        i += 1
    mid_node = None
    first_head = head
    if fast_p is None: #which means length of list is even
        second_head = slow_p
    else:
        slow_p = slow_p.next
        second_head = slow_p
    if i % 2 == 0:
        j = 0
        current = first_head 
        while j < i:
            current = current.next
            j += 1
    else:
        j = 0
        current = first_head 
        while j != i:
            current = current.next
            j += 1
    ### reversing the second half
    curr = second_head
    prev = None
    while curr:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
    second_head = prev
    rev_curr = second_head
    normal_curr = first_head
    while rev_curr:
        if rev_curr.data != normal_curr.data:
            return 0
        rev_curr = rev_curr.next
        normal_curr = normal_curr.next
    return 1