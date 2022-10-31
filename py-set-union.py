# https://www.hackerrank.com/challenges/py-set-union/problem

eng_sub = int(input())
eng_sub_roll = set(input().split())
fr_sub = int(input())
fr_sub_roll = set(input().split())
print(len(eng_sub_roll.union(fr_sub_roll)))
