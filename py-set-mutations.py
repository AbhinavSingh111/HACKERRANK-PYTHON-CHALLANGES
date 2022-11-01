# https://www.hackerrank.com/challenges/py-set-mutations/problem

n_a = int(input())
s_a = set(input().split())
n_o = int(input())
for i in range(n_o):
    opn , l_s = input().split()
    o_s = set(input().split())
    cmnd = f's_a.{opn}(o_s)'
    exec(cmnd)
print(sum(set(map(int,s_a))))
