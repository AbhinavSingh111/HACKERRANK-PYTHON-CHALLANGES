def reversePrint(llist):
    # Write your code here
    a = []
    while llist:
        a.append(llist.data)
        llist=llist.next
    a.reverse()
    for i in a:
        print(i)
        
    # or recursive appropach
    
    
    if llist:
        reversePrint(llist.next)
        print(llist.data)
