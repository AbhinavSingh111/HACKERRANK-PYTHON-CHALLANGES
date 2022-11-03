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
