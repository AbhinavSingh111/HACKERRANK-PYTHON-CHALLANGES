https://www.hackerrank.com/challenges/any-or-all/problem
n = int(input())
arr  = input().split()
l1=[arr[i]==arr[i][::-1] for i in range(len(arr)) ]
l2=[int(arr[i])>=1 for i in range(len(arr))]
#print(any([arr[i]==arr[i][::-1] for i in range(len(arr)) ])and all([int(arr[i])>=1 for i in range(len(arr))]))
# for i in range(len(arr)):
#     l1.append(arr[i]==arr[i][::-1])
# for i in range(len(arr)):
#     arr[i] = int(arr[i])
# for i in range(len(arr)):
#     l2.append(arr[i]>=1)
print(any(l1)and all(l2))

