# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

n_t_c = int(input())
for i in range(n_t_c):
    n_a = int(input())
    s_a = set(input().split())
    n_b = int(input())
    s_b = set(input().split())
    if len(s_a) == len(s_a.intersection(s_b)):
        print("True")
    else:
        print("False")
