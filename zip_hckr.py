# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
# The National University conducts an examination of  students in  subjects.
# Your task is to compute the average scores of each student.
n,x=input().split()
n,x=int(n),int(x)
s=[]
for i in range(x):
    s.append(input().split())
s = list(zip(*s))
for i in range(n):
    m = list(map(float,s[i]))
    tm = round((sum(m)/x),1)
    print(tm)
