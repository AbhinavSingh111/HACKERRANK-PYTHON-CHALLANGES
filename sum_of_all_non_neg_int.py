# program to sum all non negative integers via recursion
def sum(n):
    if n==1:
        return n
    else:
        return(n+sum(n-1))

t=True
total=0
n=int(input())
while t:
    if n<=0:
        print("Enter a positive number! ")
    else:
        t=False
print(sum(n))
