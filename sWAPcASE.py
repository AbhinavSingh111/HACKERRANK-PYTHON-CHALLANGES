def swap_case(s):
    
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#     or below solution is also apt

def swap_case(s):
    p=""
    for i in s:
        if i.islower():
            p+=i.upper()
        elif i.isupper():
            p+=i.lower()
        else:
            p+=i
            
    return p

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
