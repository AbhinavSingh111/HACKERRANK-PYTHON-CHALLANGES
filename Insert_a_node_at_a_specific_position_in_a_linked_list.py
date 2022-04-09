def insertNodeAtPosition(llist, data, position):
    i=0
    if llist is None:
        llist= SinglyLinkedListNode(data)
    else:
        temp=llist
        while i!=position-1:
            temp=temp.next
            i+=1
        new_node=SinglyLinkedListNode(data)
        new_node.next=temp.next
        temp.next=new_node
    return llist
