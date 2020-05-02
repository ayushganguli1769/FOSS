merge_head = None
merge_current = None
def merge(head_a,head_b):
    global merge_head, merge_current
    merge_head = None
    merge_current = None
    current1 = head_a
    current2 = head_b
    i = 0
    while current1 or current2:
        if current1 is None:
            while current2:
                append(current2)
                current2 = current2.next
        elif current2 is None:
            while current1:
                append(current1)
                current1 = current1.next
        elif current1.data <= current2.data:
            append(current1)
            current1 = current1.next
        else:
            append(current2)
            current2 = current2.next

    return merge_head
def append(node):
    global merge_head,merge_current 
    if merge_head is None:
        merge_head = node
        merge_current = node
    else:
        merge_current.next = node
        merge_current = merge_current.next