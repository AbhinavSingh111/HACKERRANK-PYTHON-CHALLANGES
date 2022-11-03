# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

k = int(input())
r_n = input().split()
d = {}
for i in range(len(r_n)):
    if r_n[i] in d:
        d[r_n[i]]+=1
    else:
        d[r_n[i]]=1
for key,values in d.items():
    if values==1:
        print(key)
        
#      or

k = int(input())
r_n = input().split()
r_s = set(r_n)
for i in r_s:
    r_n.remove(i)
# res = list(r_s.difference(r_n))
# print(int(res[0]))

# or

print(*(r_s.difference(r_n)))
    
