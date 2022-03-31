def split_and_join(line):
    # write your code here
    line=line.split(" ")
    line="-".join(line)
    return line

if __name__ == '__main__':
    
#     or this approach is also apt

def split_and_join(line):
    return line.replace(" ","-")

if __name__ == '__main__':
