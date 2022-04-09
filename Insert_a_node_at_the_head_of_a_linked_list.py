def insertNodeAtHead(llist, data):
    if llist is None:
        llist=SinglyLinkedListNode(data)
    else:
        new_node=SinglyLinkedListNode(data)
        new_node.next=llist
        llist=new_node
    return llist
