# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n_e = int(input())
s_e = set(input().split())
n_f = int(input())
s_f = set(input().split())
print(len(s_e.symmetric_difference(s_f)))
