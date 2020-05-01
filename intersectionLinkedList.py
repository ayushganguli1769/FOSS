def intersetPoint(head_a,head_b):
    l1 = 0
    l2 = 0
    current_l1= head_a
    current_l2 = head_b
    while current_l1 and current_l2:
        current_l1 = current_l1.next
        current_l2 = current_l2.next
        l1 += 1
        l2 += 1
    if current_l1:
        while current_l1:
            current_l1 = current_l1.next
            l1 += 1
    elif current_l2:
        while current_l2:
            current_l2 = current_l2.next
            l2 += 1
    diff = abs(l1 - l2)
    if l1 > l2:
        current_long = head_a
        current_short = head_b
    else:
        current_long = head_b
        current_short = head_a
    #bringing both of them to same length
    j = 0
    while j < diff:
        current_long = current_long.next
        j += 1
    while current_long and current_short:
        if current_long == current_short:
            return current_long
        current_long = current_long.next
        current_short = current_short.next
        
    return -1