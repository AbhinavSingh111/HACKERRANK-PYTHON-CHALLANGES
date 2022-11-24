rows, cols = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(cols, '-') for i in range(rows//2)]
print('\n'.join(pattern + ['WELCOME'.center(cols, '-')] + pattern[::-1]))
