def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    l=''.join(l)
    return l
    

if __name__ == '__main__':
