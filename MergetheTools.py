def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        uniq = ''
        for c in string[i : i+k]:
            if (c not in uniq):
                uniq+=c
        print(uniq)
        
#  alternate method
    your code goes here
    l=[]
    i=0 
    w=len(string)//k
    while i<len(string):
        j = string[i:k+i]
        l.append(j)
        i+=k
    for i in range(w):
        s=l[i]
        q=[]
        for j in s:
            if j in q:
                pass
            else:
                q.append(j)
        q=''.join([str(e) for e in q])
        print(q)
 
