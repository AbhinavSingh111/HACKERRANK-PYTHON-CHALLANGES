# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

s_a = set(input().split())
res = "True"
for i in range(int(input())):
    s_o = set(input().split())
    if s_o.issubset(s_a) and len(s_a)>len(s_o):
        continue
    else:
        res = "False"
        break
print(res)
