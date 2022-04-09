def insertNodeAtTail(head, data):
    if head is None:
        head = SinglyLinkedListNode(data)
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = SinglyLinkedListNode(data)
    return head
