# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

e_num = int(input())
e_roll = set(input().split())
f_num = int(input())
f_roll = set(input().split())
print(len(f_roll.intersection(e_roll)))
