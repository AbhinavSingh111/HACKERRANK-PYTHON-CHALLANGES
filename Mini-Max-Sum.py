# https://www.hackerrank.com/challenges/mini-max-sum/problem

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# easy and simple python approach:

def miniMaxSum(arr):
    # Write your code here
    maximum_sum = -float('inf')
    minimum_sum = float('inf')
    total_sum = sum(arr)
    for i in arr:
        temp_sum = total_sum-i
        if temp_sum>maximum_sum:
            maximum_sum = temp_sum
        if temp_sum<minimum_sum:
            minimum_sum = temp_sum
    print(int(minimum_sum) , int(maximum_sum))
    
#     2 liner , easy and simple python approach:
def miniMaxSum(arr):
    ans = [sum(arr)-i for i in arr]
    print(min(ans),max(ans))
    
# 1 liner
def miniMaxSum(arr):
   print(sum(arr)-max(arr),sum(arr)-min(arr))
