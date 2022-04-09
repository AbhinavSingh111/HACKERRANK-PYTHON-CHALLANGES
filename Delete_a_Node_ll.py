  i=0
    if llist is None:
        return None
    elif position==0:
        llist=llist.next
    else:
        temp=llist
        while i!=position-1:
            temp=temp.next
            i+=1
        temp.next=temp.next.next
    return llist
  
#   recursive approach

if position==0:
        return llist.next
    llist.next = deleteNode(llist.next,position-1)
    return llist
