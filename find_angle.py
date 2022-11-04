# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
from math import (atan, degrees)

ab = int(input())
bc = int(input())

theta = degrees(atan(ab/bc))
print(f"{round(theta)}"u"\xb0")
