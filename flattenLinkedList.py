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
                current2 = current2.bottom
        elif current2 is None:
            while current1:
                append(current1)
                current1 = current1.bottom
        elif current1.data <= current2.data:
            append(current1)
            current1 = current1.bottom
        else:
            append(current2)
            current2 = current2.bottom

    return merge_head
def append(node):
    global merge_head,merge_current 
    if merge_head is None:
        merge_head = node
        merge_current = node
    else:
        merge_current.bottom = node
        merge_current = merge_current.bottom
def flatten(root):
    curr = root
    while curr and curr.next:
        head_a = curr
        head_b = curr.next
        merge_list_next = curr.next.next
        head_merged_list = merge(head_a,head_b)
        head_merged_list.next = merge_list_next
        curr = head_merged_list
    return curr
